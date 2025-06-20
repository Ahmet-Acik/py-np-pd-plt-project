# server.py
import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server listening...")
conn, addr = server_socket.accept()
print("Connected by", addr)
data = conn.recv(1024)
print("Received:", data.decode())
conn.sendall(b'Hello, client!')
conn.close()