import socket

HOST = '127.0.0.1'
PORT = 5555
nickname = input("Choose your nickname: ")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))