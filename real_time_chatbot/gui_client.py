import tkinter as tk
from tkinter import scrolledtext, simpledialog
import socket
import threading

class ChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.root = tk.Tk()
        self.root.title("Real-Time Chat App")

        self.chat_label = tk.Label(self.root, text="Chat:", font=("Arial", 12))
        self.chat_label.pack(padx=10, pady=5)

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.msg_entry = tk.Entry(self.root, font=("Arial", 12))
        self.msg_entry.pack(padx=10, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_message)

        self.username = simpledialog.askstring("Username", "Enter your username", parent=self.root)

        self.connect_to_server()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def connect_to_server(self):
        try:
            self.client_socket.connect(("localhost", 5555))
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            self.display_message(f"Connection error: {e}")

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                self.display_message(msg)
            except:
                self.display_message("Disconnected from server.")
                break

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        self.msg_entry.delete(0, tk.END)
        full_msg = f"{self.username}: {msg}"
        try:
            self.client_socket.send(full_msg.encode())
        except:
            self.display_message("Failed to send message.")

    def display_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + '\n')
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')

    def on_close(self):
        try:
            self.client_socket.close()
        except:
            pass
        self.root.destroy()

if __name__ == "__main__":
    ChatClient()
