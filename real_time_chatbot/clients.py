# realtime_chatbot/clients.py

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(msg)
        except:
            print("Disconnected from server.")
            break

def send_messages(client_socket, username):
    while True:
        msg = input("")
        full_msg = f"{username}: {msg}"
        client_socket.send(full_msg.encode())

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5555))

    username = input("Enter your username: ")
    print(f"Welcome {username}! Start chatting...")

    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client, username))
    send_thread.start()

if __name__ == "__main__":
    start_client()
