import socket               # Import socket module
import time

# make the socket
s = socket.socket()         # Create a socket object
host = '0.0.0.0' # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    print("Receiving...")
    fname = c.recv(1024)
    print(fname)
    f = open(fname,'wb')

    # start receiving file
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
        if len(l) < 1024:
            break
        time.sleep(0.2)

    f.close()
    print("Done Receiving")
    s.shutdown(socket.SHUT_WR)
    out = 'Thank you for connecting'
    c.sendall(out.encode('utf-8'))
    c.close()
s.close()
