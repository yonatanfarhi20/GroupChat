import socket


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred! {e}")
            client.close()
            break


HOST = '127.0.0.1'
PORT = 5555
nickname = input("Choose your nickname: ")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

