"""Same-origin introduction delivery. Credentials and recipients stay server-side."""
from email.headerregistry import Address
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler
import json
import os
import re
import smtplib
import ssl
from urllib.parse import urlsplit

MAX_BODY = 24 * 1024
LIMITS = {"name": 120, "email": 254, "organisation": 200,
          "opportunity": 6000, "contribution": 3000}
STARTING_POINTS = {"expertise", "company", "capital", "assets", "founder", "other"}


def valid_email(value):
    if not isinstance(value, str) or len(value) > 254 or not value.isascii():
        return False
    if not re.fullmatch(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+", value):
        return False
    local, domain = value.rsplit("@", 1)
    if len(local) > 64 or local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    labels = domain.split(".")
    if len(labels) < 2 or any(not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?", label) for label in labels):
        return False
    try:
        return Address(addr_spec=value).addr_spec == value
    except ValueError:
        return False


def allowed_origins():
    origins = {"https://castelein.eu.com", "https://www.castelein.eu.com"}
    for key in ("VERCEL_URL", "VERCEL_PROJECT_PRODUCTION_URL"):
        host = os.environ.get(key, "")
        if re.fullmatch(r"[A-Za-z0-9.-]+", host):
            origins.add("https://" + host)
    for origin in os.environ.get("CONTACT_ALLOWED_ORIGINS", "").split(","):
        origin = origin.strip()
        try:
            parsed = urlsplit(origin)
            if parsed.netloc and not (parsed.path or parsed.query or parsed.fragment or parsed.username or parsed.password):
                if parsed.scheme == "https" or (parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1"}):
                    origins.add(origin)
        except ValueError:
            pass
    return origins


def validate(payload):
    if not isinstance(payload, dict) or set(payload) - set(LIMITS) - {"startingPoint", "locale", "website"}:
        raise ValueError("invalid")
    if payload.get("website", "") != "":
        raise ValueError("invalid")
    fields = {}
    for key, limit in LIMITS.items():
        value = payload.get(key, "")
        if not isinstance(value, str) or len(value) > limit:
            raise ValueError("invalid")
        value = value.strip()
        if any((ord(char) < 32 and char not in "\n\t") or ord(char) == 127 for char in value):
            raise ValueError("invalid")
        if key in {"name", "email", "organisation"} and any(char in value for char in "\n\t"):
            raise ValueError("invalid")
        fields[key] = value
    if not fields["name"] or not fields["opportunity"] or not valid_email(fields["email"]):
        raise ValueError("invalid")
    if payload.get("startingPoint") not in STARTING_POINTS or payload.get("locale") not in {"en", "pt", "es"}:
        raise ValueError("invalid")
    fields.update(startingPoint=payload["startingPoint"], locale=payload["locale"])
    return fields


def mail_config():
    if os.environ.get("ENQUIRY_FORMS_ENABLED") != "true":
        raise ValueError("unavailable")
    values = {key: os.environ.get(key, "") for key in ("SMTP_HOST", "SMTP_USER", "SMTP_PASS", "SMTP_FROM")}
    if not all(values.values()) or not valid_email(values["SMTP_FROM"]):
        raise ValueError("unavailable")
    host = values["SMTP_HOST"]
    if len(host) > 253 or not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        raise ValueError("unavailable")
    port = int(os.environ.get("SMTP_PORT", "587"))
    recipient = os.environ.get("ENQUIRY_PERSONAL_TO", "paul@skaler.pt")
    if port not in {465, 587} or not valid_email(recipient):
        raise ValueError("unavailable")
    return values, port, recipient


def deliver(fields, config):
    values, port, recipient = config
    message = EmailMessage()
    message["From"] = values["SMTP_FROM"]
    message["To"] = recipient
    message["Reply-To"] = fields["email"]
    message["Subject"] = "Castelein website introduction"
    message.set_content("\n\n".join(f"{key}: {fields[key]}" for key in
                        ("name", "email", "organisation", "startingPoint", "locale", "opportunity", "contribution")))
    context = ssl.create_default_context()
    client = None
    try:
        if port == 465:
            client = smtplib.SMTP_SSL(values["SMTP_HOST"], port, timeout=10, context=context)
        else:
            client = smtplib.SMTP(values["SMTP_HOST"], port, timeout=10)
            client.ehlo()
            client.starttls(context=context)
            client.ehlo()
        client.login(values["SMTP_USER"], values["SMTP_PASS"])
        refused = client.send_message(message, from_addr=values["SMTP_FROM"], to_addrs=[recipient])
        if refused:
            raise smtplib.SMTPRecipientsRefused(refused)
    finally:
        if client is not None:
            try:
                client.close()
            except OSError:
                pass


class handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        # Avoid writing request details or enquiry content into application logs.
        pass

    def respond(self, status, code):
        body = json.dumps({"ok": status == 200, "code": code}).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        if status == 405:
            self.send_header("Allow", "POST")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self.respond(405, "method")

    def do_POST(self):
        if self.headers.get("Origin") not in allowed_origins():
            self.respond(403, "origin")
            return
        if self.headers.get_content_type() != "application/json" or self.headers.get("Transfer-Encoding"):
            self.respond(415, "content_type")
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.respond(400, "invalid")
            return
        if not 0 < size <= MAX_BODY:
            self.respond(413, "too_large")
            return
        try:
            self.connection.settimeout(5)
            body = self.rfile.read(size)
            if len(body) != size:
                raise ValueError("invalid")
            fields = validate(json.loads(body))
        except (ValueError, UnicodeDecodeError, TypeError, OSError):
            self.respond(400, "invalid")
            return
        try:
            config = mail_config()
        except (ValueError, OverflowError):
            self.respond(503, "unavailable")
            return
        try:
            deliver(fields, config)
        except (OSError, smtplib.SMTPException):
            self.respond(502, "delivery_failed")
            return
        self.respond(200, "sent")
