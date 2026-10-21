"""Local static preview plus the real enquiry handler. No mail is sent without config."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import os
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from api.enquiry import handler as EnquiryHandler


class PreviewHandler(EnquiryHandler, SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?', 1)[0] == '/api/enquiry':
            return EnquiryHandler.do_GET(self)
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path != '/api/enquiry':
            return self.respond(404, 'not_found')
        return EnquiryHandler.do_POST(self)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4187)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(PreviewHandler, directory=str(ROOT / 'dist')))
    port = server.server_address[1]
    local = f'http://127.0.0.1:{port},http://localhost:{port}'
    os.environ['CONTACT_ALLOWED_ORIGINS'] = ','.join(filter(None, [os.environ.get('CONTACT_ALLOWED_ORIGINS'), local]))
    print(f'Preview with enquiry API: http://127.0.0.1:{port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
