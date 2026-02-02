# secure-chat
Secure Chat Application

The goal of my project was to develop an application that allows people to chat in real-time, but I wanted to also explore how computer networks and security function in practical terms. 
So instead of just learning about these concepts through text books, I have built a real time working client server model allowing multiple users to communicate with each other.


# What the project does
-The project is an application that enables several users to access a single chat room from different terminals of the same computer.
-There is one program that acts as a server, which handles all the connections.
-There are other programs that act as clients, which connect to the server and send messages.
-Each message is encrypted before it is sent, ensuring that the messages are secure.
-The messages are sent to all the connected users in real time.

# Key concepts I learned
While building this project, I gained practical experience in:
-Socket programming – understanding how machines communicate over a network
-Client–server architecture – how real applications like chat apps are structured
-Multithreading – handling multiple users at the same time
-Basic cryptography – using symmetric encryption (Fernet) to secure messages
-Error handling and debugging in networks
-This project helped me connect my theoretical knowledge of Computer Networks and Security with real implementation.

# How to run the project
Step 1 — Install required library
pip install cryptography

Step 2 — Start the server
Open a terminal and run:
python server.py
You should see a message that the server has started.

Step 3 — Start clients
Open new terminals and run:
python client.py
Enter your name when prompted and start chatting.
You can open multiple clients to simulate different users.

# This project's files
All connections and message broadcasting are managed by server.py.
client.py – allows users to connect and chat
crypto.py – handles encryption and decryption of messages

# Upcoming enhancements
If I continue this project, I plan to add:
Users exchanging private messages
Messages with timestamps
Display of users who are currently active
Storage of chat history
Secure key exchange instead of a fixed key
