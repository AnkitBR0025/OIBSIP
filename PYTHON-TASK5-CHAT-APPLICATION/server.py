import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Server started. Waiting for two clients to connect...")

clients = []
names = []


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))


def handle_client(client_socket, name):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                raise ConnectionResetError
            full_msg = f"[{get_time()}] {name}: {msg}"
            print(full_msg)
            broadcast(full_msg, client_socket)
        except:
            print(f"{name} has disconnected.")
            clients.remove(client_socket)
            names.remove(name)
            broadcast(f"[{get_time()}] Server: {name} has left the chat.", client_socket)
            client_socket.close()
            break


while len(clients) < 2:
    client_socket, addr = server.accept()

    client_socket.send("NAME".encode('utf-8'))
    name = client_socket.recv(1024).decode('utf-8')

    names.append(name)
    clients.append(client_socket)

    print(f"{name} connected from {addr}")
    broadcast(f"[{get_time()}] Server: {name} has joined the chat.", client_socket)

    thread = threading.Thread(target=handle_client, args=(client_socket, name))
    thread.start()

print("Both clients connected. Chat is live.")
