from http.server import BaseHTTPRequestHandler, HTTPServer
import json

import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5005,
                    help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)


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
        json_data = json.loads(payload)
        getplayerinfoforteam("name", json_data)

    def log_message(self, format, *args):
        """Prevents requests from printing into the console."""
        return


def gpfp(path, dict):
    path = path.split("/")
    output = dict
    for path_item in path:
        try:
            output = output[path_item]
        except:
            output = "N/A"
            pass
    return str(output)


def getplayerinfoforteam(param, dict):
    for team in dict["player"]:
        for player in dict["player"][team]:
            client.send_message("/"+str(param) + str(player)[6:7], dict["player"][team][player][str(param)])


server = HTTPServer(('192.168.1.219', 3000), MyRequestHandler)

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    pass

server.server_close()
