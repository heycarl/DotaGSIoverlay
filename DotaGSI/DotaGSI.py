from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from json import loads, dumps



class MyRequestHandler(BaseHTTPRequestHandler):
    """DOTA's requests handler."""

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
        parsed_string = json.loads(payload)
        print(getParametrFromPath("hero/team3/player5", parsed_string))

    def log_message(self, format, *args):
        """Prevents requests from printing into the console."""
        return
    def uploadData():
        print(getParametrFromPath("hero/team3/player5", parsed_string))


def getParametrFromPath(path, dict):
    path = path.split("/")
    output = dict
    for path_item in path:
        try:
            output = output[path_item]
        except:
            output = "N/A"
            pass
    return str(output)


class MyServer(HTTPServer):
    """Server storing DOTA's information."""

    payload = None


server = MyServer(('localhost', 3000), MyRequestHandler)

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    pass

server.server_close()
