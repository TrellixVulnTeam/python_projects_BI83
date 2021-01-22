import socket
# A socket is an end point that recieves data, sockets simple recieve the data from an IP and a Port

# AF_INET = is used for IPV4 and SOCK_STREAM = is used for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("78.145.156.195", 9090)) # As this is the client we want to connect to a specific IP and Port

# BEcause on the server we sent a message to connections we need a way to accept that message/ recieve it
msg = s.recv(1024)
# 1024 is our buffer as we are using a stream of data and we must decide how big a chunk of data we want to recieve.

print(msg.decode("utf-8")) # As we encoded the message as a UTF-8 we must decode it here so we can read it