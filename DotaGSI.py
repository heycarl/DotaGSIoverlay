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
        getplayerinfoforteam("kill_streak", json_data)
        getplayerinfoforteam("gpm", json_data)
        getplayerinfoforteam("xpm", json_data)
        getplayerinfoforteam("wards_purchased", json_data)
        getplayerinfoforteam("wards_placed", json_data)
        getplayerinfoforteam("wards_destroyed", json_data)
        getplayerinfoforteam("runes_activated", json_data)
        getplayerinfoforteam("camps_stacked", json_data)
        getheroinfoforteam("name", json_data)
        getheroinfoforteam("level", json_data)
        getheroinfoforteam("alive", json_data)
        getheroinfoforteam("buyback_cost", json_data)
        getheroinfoforteam("smoked", json_data)
        getheroinfoforteam("selected_unit", json_data)

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
    try:
        for team in dict["player"]:
            for player in dict["player"][team]:
                client.send_message("/"+str(param) + str(player)[-1:], dict["player"][team][player][str(param)])
    except KeyError:
        return


def getheroinfoforteam(param, dict):
    try:
        for team in dict["hero"]:
            for hero in dict["hero"][team]:
                if param == "name":
                    client.send_message("/" + "hero_name" + str(hero)[-1:], dict["hero"][team][hero][str(param)])
                else:
                    client.send_message("/" + str(param) + str(hero)[-1:], dict["hero"][team][hero][str(param)])
    except KeyError:
        return


server = HTTPServer(('192.168.1.219', 3000), MyRequestHandler)

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    pass

server.server_close()
