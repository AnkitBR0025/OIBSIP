# Name:- Ankit Kumar Pandey
# Track:- python Programming
# Task Title:- Chat Application




import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def get_time():
    return datetime.now().strftime("%H:%M")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NAME":
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break


name = input("Enter your name: ")

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    try:
        message = input()
        client.send(message.encode('utf-8'))
    except:
        client.close()
        break
