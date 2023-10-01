import os
import socket
import threading


ip = input("Введите IP: ")

# подключаемся к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 1303))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("Error!")
        client.close()
        break

os.system('clear')

receive()