import socket

HOST = "192.168.1.7"
PORT = 5231

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

while True:

    print(f"Connected To {address}")

    cmd_input = input("Enter a Command: ")

    client.send(cmd_input.encode("utf-8"))
    print(client.recv(1024).decode("utf-8"))