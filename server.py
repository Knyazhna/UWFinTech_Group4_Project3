from socket import socket
import socketserver
import deployer2
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8080

def handle (action):
    interfaceList = deployer2.deploy()
    print(interfaceList)
    
    return interfaceList

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        params = urllib.parse.parse_qs(self.path[2:])
        print(self.path)
        print(params)

        action = params["action"]
        # reward = params["reward"]
        # nft721 = params["nft721"]
        # owner = params["owner"]
        interfaces = handle(action)



        message = "Hello Scrubs!"
        self.wfile.write(bytes(message, "utf8"))

# with socketserver.TCPServer(("", PORT), handler) as httpd:
#     print("serving at port",PORT)
#     http.serve_forever()
with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
    print("done")

# handle("banana")