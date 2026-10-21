"""No external mail is sent: HTTP integration and SMTP contract tests."""
from contextlib import contextmanager
from http.client import HTTPConnection
from http.server import HTTPServer
import json
import os
import smtplib
import socket
import threading
import unittest
from unittest.mock import patch

from api.enquiry import MAX_BODY, allowed_origins, deliver, handler, mail_config, valid_email

ORIGIN = 'https://www.castelein.eu.com'
ENV = {'ENQUIRY_FORMS_ENABLED': 'true', 'SMTP_HOST': 'smtp.example.test',
       'SMTP_PORT': '587', 'SMTP_USER': 'test-user', 'SMTP_PASS': 'test-only',
       'SMTP_FROM': 'website@example.test', 'ENQUIRY_PERSONAL_TO': 'recipient@example.test'}
DATA = {'name': 'Test Visitor', 'email': 'visitor@example.test', 'organisation': '',
        'startingPoint': 'expertise', 'opportunity': 'A test introduction.',
        'contribution': '', 'locale': 'en', 'website': ''}


@contextmanager
def server():
    httpd = HTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield httpd.server_port
    finally:
        httpd.shutdown()
        thread.join()
        httpd.server_close()


def request(port, data=DATA, origin=ORIGIN, content_type='application/json', raw=None, method='POST'):
    connection = HTTPConnection('127.0.0.1', port, timeout=3)
    body = json.dumps(data).encode() if raw is None else raw
    headers = {'Content-Type': content_type}
    if origin is not None:
        headers['Origin'] = origin
    connection.request(method, '/api/enquiry', body, headers)
    response = connection.getresponse()
    result = response.status, json.loads(response.read()), dict(response.getheaders())
    connection.close()
    return result


class EnquiryTests(unittest.TestCase):
    def test_accepted_mail_is_the_only_success(self):
        with patch.dict(os.environ, ENV, clear=True), patch('api.enquiry.smtplib.SMTP') as smtp, server() as port:
            smtp.return_value.send_message.return_value = {}
            code, result, headers = request(port)
            self.assertEqual((code, result), (200, {'ok': True, 'code': 'sent'}))
            self.assertEqual(headers['Cache-Control'], 'no-store')
            client = smtp.return_value
            self.assertEqual([call[0] for call in client.method_calls], ['ehlo', 'starttls', 'ehlo', 'login', 'send_message', 'close'])
            mail = client.send_message.call_args.args[0]
            self.assertEqual(str(mail['Reply-To']), DATA['email'])
            self.assertEqual(str(mail['To']), ENV['ENQUIRY_PERSONAL_TO'])
            self.assertIn(DATA['opportunity'], mail.get_content())
            self.assertNotIn(ENV['SMTP_PASS'], mail.as_string())

    def test_tls465_and_fixed_recipient(self):
        with patch.dict(os.environ, {**ENV, 'SMTP_PORT': '465'}, clear=True), patch('api.enquiry.smtplib.SMTP_SSL') as smtp:
            smtp.return_value.send_message.return_value = {}
            deliver(DATA, mail_config())
            self.assertIsNotNone(smtp.call_args.kwargs['context'])
            self.assertEqual(smtp.return_value.send_message.call_args.kwargs['to_addrs'], [ENV['ENQUIRY_PERSONAL_TO']])
            smtp.return_value.starttls.assert_not_called()

    def test_configuration_disabled_or_missing_never_sends(self):
        for changes in ({'ENQUIRY_FORMS_ENABLED': 'false'}, {'SMTP_PASS': ''}, {'SMTP_FROM': 'bad'}, {'SMTP_PORT': '25'}, {'SMTP_PORT': 'invalid'}):
            with self.subTest(changes=changes), patch.dict(os.environ, {**ENV, **changes}, clear=True), patch('api.enquiry.smtplib.SMTP') as smtp, server() as port:
                code, result, _ = request(port)
                self.assertEqual((code, result['ok'], result['code']), (503, False, 'unavailable'))
                smtp.assert_not_called()

    def test_delivery_failures_never_report_success(self):
        for failure in (smtplib.SMTPAuthenticationError(535, b'No'), smtplib.SMTPNotSupportedError('STARTTLS'), TimeoutError(), smtplib.SMTPRecipientsRefused({'recipient@example.test': (550, b'No')})):
            with self.subTest(failure=type(failure).__name__), patch.dict(os.environ, ENV, clear=True), patch('api.enquiry.deliver', side_effect=failure), server() as port:
                code, result, _ = request(port)
                self.assertEqual((code, result), (502, {'ok': False, 'code': 'delivery_failed'}))

    def test_recipient_refusal_mapping_is_failure(self):
        with patch.dict(os.environ, ENV, clear=True), patch('api.enquiry.smtplib.SMTP') as smtp:
            smtp.return_value.send_message.return_value = {'recipient@example.test': (550, b'No')}
            with self.assertRaises(smtplib.SMTPRecipientsRefused):
                deliver(DATA, mail_config())
            smtp.return_value.close.assert_called_once()

    def test_bad_fields_rejected_before_configuration_or_smtp(self):
        changes = ({'name': ''}, {'name': 'Test\nBcc: someone'}, {'email': 'bad'}, {'email': 'person@example.test\r\nBcc:x@example.test'}, {'opportunity': ''}, {'opportunity': 'x' * 6001}, {'name': 1}, {'name': 'Bad\x7f'}, {'website': 'filled'}, {'startingPoint': 'invalid'}, {'locale': 'xx'}, {'recipient': 'attacker@example.test'})
        with patch.dict(os.environ, ENV, clear=True), patch('api.enquiry.smtplib.SMTP') as smtp, server() as port:
            for change in changes:
                with self.subTest(change=change):
                    code, result, _ = request(port, {**DATA, **change})
                    self.assertEqual((code, result['ok']), (400, False))
            smtp.assert_not_called()

    def test_exact_origin_required(self):
        with patch.dict(os.environ, ENV, clear=True), server() as port:
            for origin in (None, 'null', 'https://www.castelein.eu.com.evil.test', 'https://evil.test', ORIGIN + '/'):
                with self.subTest(origin=origin):
                    self.assertEqual(request(port, origin=origin)[0], 403)

    def test_preview_origins_are_explicit(self):
        with patch.dict(os.environ, {'VERCEL_URL': 'exact-preview.vercel.app', 'CONTACT_ALLOWED_ORIGINS': 'https://allowed.example.test,http://evil.test,https://other.test/path,http://127.0.0.1:4187'}, clear=True):
            origins = allowed_origins()
            self.assertIn('https://exact-preview.vercel.app', origins)
            self.assertIn('https://allowed.example.test', origins)
            self.assertIn('http://127.0.0.1:4187', origins)
            self.assertNotIn('http://evil.test', origins)
            self.assertNotIn('https://other.test/path', origins)

    def test_malformed_large_and_wrong_content_type(self):
        with server() as port:
            self.assertEqual(request(port, raw=b'{broken')[0], 400)
            self.assertEqual(request(port, raw=b'\xff')[0], 400)
            self.assertEqual(request(port, raw=b'x' * (MAX_BODY + 1))[0], 413)
            self.assertEqual(request(port, content_type='text/plain')[0], 415)
            code, _, headers = request(port, method='GET')
            self.assertEqual(code, 405)
            self.assertEqual(headers['Allow'], 'POST')

    def test_truncated_body_is_rejected(self):
        with server() as port:
            connection = socket.create_connection(('127.0.0.1', port), timeout=3)
            connection.sendall((f'POST /api/enquiry HTTP/1.1\r\nHost: localhost\r\nOrigin: {ORIGIN}\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n{{').encode())
            connection.shutdown(socket.SHUT_WR)
            self.assertIn(b'400', connection.recv(4096).split(b'\r\n', 1)[0])
            connection.close()

    def test_starttls_failure_prevents_credentials_and_mail(self):
        with patch.dict(os.environ, ENV, clear=True), patch('api.enquiry.smtplib.SMTP') as smtp:
            client = smtp.return_value
            client.starttls.side_effect = smtplib.SMTPNotSupportedError('No TLS')
            with self.assertRaises(smtplib.SMTPNotSupportedError):
                deliver(DATA, mail_config())
            client.login.assert_not_called()
            client.send_message.assert_not_called()
            client.close.assert_called_once()

    def test_email_validation_rejects_header_and_domain_tricks(self):
        for address in ('a..b@example.test', '.a@example.test', 'a@example..test', 'a@-example.test', 'a@example.test\n', 'Name <a@example.test>', 'a@localhost'):
            with self.subTest(address=address):
                self.assertFalse(valid_email(address))
        self.assertTrue(valid_email('first.last+tag@example.test'))


if __name__ == '__main__':
    unittest.main()
