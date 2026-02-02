import socket
import threading
from crypto import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive_messages():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            message = decrypt_message(encrypted_msg)

            if message == "NAME":
                client.send(encrypt_message(name))
            else:
                print(message)

        except:
            print("Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        message = input()
        full_message = f"{name}: {message}"
        client.send(encrypt_message(full_message))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_messages()
