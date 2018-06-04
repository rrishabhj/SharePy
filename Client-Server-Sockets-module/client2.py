import socket               # Import socket module
import time
import os

s = socket.socket()         # Create a socket object
host =  '192.168.0.101'
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
# s.send("Hello server!")
faddress = '/home/ankit/cowrks/rishabh2.png'
fname = os.path.basename(faddress)
s.send(fname)
time.sleep(0.2)

f = open(faddress,'rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
    time.sleep(0.2)

f.close()
print("Done Sending")
print(s.recv(1024))
s.close()                  # Close the socket when done
