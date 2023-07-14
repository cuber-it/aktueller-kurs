import socket

url = r"https://datausa.io/api/data?drilldowns=Nation&measures=Population"

def http_get(url):
    _, _, host, path = url.split('/', 3)
    sock = socket.socket()
    sock.connect((host, 80))
    request = 'GET /{} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(path, host)
    sock.send(request.encode())
    response = ''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk.decode()
        chunk = sock.recv(4096)
    return response

print(http_get(url))
