import socket
import threading
from crypto import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

def broadcast(message):
    try:
        plain_text = decrypt_message(message)
        encrypted_msg = encrypt_message(plain_text)

        for client in clients:
            client.send(encrypted_msg)

    except Exception as e:
        print("Broadcast error:", e)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            name = names[index]

            clients.remove(client)
            names.remove(name)
            client.close()

            # Send encrypted "left" message
            broadcast(encrypt_message(f"{name} left the chat."))
            break

def receive_connections():
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask for name (encrypted)
        client.send(encrypt_message("NAME"))

        # Receive encrypted name
        encrypted_name = client.recv(1024)
        name = decrypt_message(encrypted_name)

        names.append(name)
        clients.append(client)

        print(f"Name of client is {name}")

        # Broadcast join message (encrypted)
        broadcast(encrypt_message(f"{name} joined the chat!"))

        # Confirm connection (encrypted)
        client.send(encrypt_message("Connected to server."))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
