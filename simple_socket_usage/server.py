import socket
# A socket is an end point that recieves data, sockets simple recieve the data from an IP and a Port

# AF_INET = is used for IPV4 and SOCK_STREAM = is used for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# You need to bind the socket, in this case we are binding it to a tuple which contains (IP, Port)
s.bind(("78.145.156.195", 9090))

# Since this is the server file it needs to be prepared to recieve incoming connections
s.listen(5) # It will prepare and leave a queue for connections (5)

while True: # This means the server will be actively listening
    clientsocket, address = s.accept() # simple means anyone that connects will be accepted entry and can connect
    #clientsocket will store the client socket object and address will store where they are coming from (IP address)
    print (f"Connection from: {address} Has been Established!") #Message for server
    clientsocket.send(bytes("Welcome To Server", "utf-8")) #Sends message to connected client, encoded as utf-8.
