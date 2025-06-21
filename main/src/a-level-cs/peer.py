# peer.py
import socket
import threading

def listen():
    s = socket.socket()
    s.bind(('localhost', 12346))
    s.listen(1)
    conn, addr = s.accept()
    print("Received:", conn.recv(1024).decode())
    conn.close()

def send():
    s = socket.socket()
    s.connect(('localhost', 12346))
    s.sendall(b'Hello from peer!')
    s.close()

threading.Thread(target=listen).start()
send()
# This code sets up a simple peer-to-peer communication using sockets.
