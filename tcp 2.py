import socket
import threading
def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
        except:
            break
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1234))
threading.Thread(target=receive_message, args=(client,)).start()
while True:
    message = input("Send the Message: ")
    client.send(message.encode('utf-8'))