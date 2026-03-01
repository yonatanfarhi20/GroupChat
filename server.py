import socket

HOST = '127.0.0.1'
PORT= 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print(f"Server is listening on {HOST}:{PORT}...")