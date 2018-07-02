#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class


class simplisticHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # GET
    def do_GET(self):
        # Send headers
        self._set_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_HEAD(self):
        # Send headers
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        # Send headers
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


def run(port=9000):
    print('starting server on port {}'.format(port))

    # Server settings
    # server_address = ('127.0.0.1', port)
    server_address = ('', port)
    httpd = HTTPServer(server_address, simplisticHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
