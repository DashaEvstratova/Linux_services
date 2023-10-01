import os
import socket
import datetime
import threading

# данные для подключения
host = '127.0.0.1'
port = 1303

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()

clients = []


def broadcast(client, message):
        client.send(message)


def receive():
    while True:
        client, address = server.accept()

        date = datetime.datetime.now()
        message = date.strftime("%Y-%m-%d %H:%M:%S")
        client.send(message.encode('ascii'))
        client.close()

os.system('clear')

receive()