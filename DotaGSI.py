from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import transfer


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        """Receive DOTA2's informations."""
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        self.parse_payload(body)
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()

    # Parsing and actions
    def parse_payload(self, payload):
        """Search payload."""
        transfer.json_data = json.loads(payload)

    def log_message(self, format, *args):
        """Prevents requests from printing into the console."""
        return


server = HTTPServer(('192.168.1.219', 3000), MyRequestHandler)

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    pass

server.server_close()
