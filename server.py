import socket

HOST = '127.0.0.1'
PORT= 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print(f"Server is listening on {HOST}:{PORT}...")

def remove(client):
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f'{nickname} left the chat!'.encode('utf-8'), None)

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except Exception as e:
                print(f"Connection error: {e}")
                remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            index = clients.index(client)
            nickname = nicknames[index]
            formatted_message = f'{nickname}: '.encode('utf-8') + message
            broadcast(formatted_message, client)
        except Exception as e:
            print(f"User disconnected: {e}")
            remove(client)
            break