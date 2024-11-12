import socket, threading
def handle_client(sock):
    while msg := sock.recv(1024).decode('utf-8'):
        print(f"Received: {msg}")
        broadcast(msg, sock)
    clients.remove(sock); sock.close()
def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg.encode('utf-8'))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1234)); server.listen(5)
clients = []
print("TCP Server listening on port 1234...")
while True:
    sock, addr = server.accept(); print(f"Connected: {addr}")
    clients.append(sock)
    threading.Thread(target=handle_client, args=(sock,)).start()    
