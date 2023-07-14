from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        query = urlparse.urlparse(self.path).query
        message = f'You said: {query}'
        self.wfile.write(bytes(message, "utf8"))

def run(server_class=HTTPServer, handler_class=EchoHandler):
    server_address = ('', 8031)
    httpd = server_class(server_address, handler_class)
    print('Starting echo server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
