import socket
from wireless import Wireless
import time

# Connecting to the incoming client to receive file

# Scan WIFI for target ssid
from access_points import get_scanner
wifi_scanner = get_scanner()
list = wifi_scanner.get_access_points()

# setting the targer Device
target = 'Rishabh'
pass = 'jindal@1234'
target_ssid = ''
for x in mylist:
    print(x.ssid + '\n')
    if x.ssid == target:
        target_ssid = x.ssid;

# Connecting to target ssid
wireless = Wireless()
wireless.connect(ssid=target, password=pass)

# Wait untill connection
time.sleep(5)
print("Connecting....")


# make the socket
s = socket.socket()
host = '0.0.0.0'
port = 12345
s.bind((host, port))
f = open('received_file.png','wb')
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    print("Receiving...")
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
        if len(l) < 1024:
            break

    f.close()
    print("Done Receiving")
    s.shutdown(socket.SHUT_WR)
    out = 'Thank you for connecting'
    c.sendall(out.encode('utf-8'))
    c.close()
s.close()
