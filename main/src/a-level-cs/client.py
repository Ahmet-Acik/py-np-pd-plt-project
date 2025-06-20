# client.py
import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 12345))
client_socket.sendall(b'Hello, server!')
data = client_socket.recv(1024)
print("Received:", data.decode())
client_socket.close()