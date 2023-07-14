import socket
import paramiko

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("localhost", 2222))

transport = paramiko.Transport(sock)

transport.start_client(timeout=10)

transport.auth_password("paramiko", "password")

session = transport.open_session(timeout=10)



session.invoke_shell()

session.send("ls -l /\n")
while True:
    resp = session.recv(4096).decode("utf-8")
    if not resp:
        break
    print(resp)
