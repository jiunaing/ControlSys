#This is a client socket to connect to the server
#to 50000 is the port to be decided
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print ('Received', repr(data))
