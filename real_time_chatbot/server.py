import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5556))
    server.listen()
    print("Server started on port 5556")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected with {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
