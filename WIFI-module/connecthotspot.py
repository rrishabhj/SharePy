from wireless import Wireless
from access_points import get_scanner

# Scan WIFI for target ssid
wifi_scanner = get_scanner()
mylist = wifi_scanner.get_access_points()

# setting the targer Device
target = 'dlink'
passw= 'ankit@1234'
target_ssid = ''

print("Available WiFi Networks")
for x in mylist:
    print(x.ssid + '\n')
    if x.ssid == target:
        target_ssid = x.ssid;

print("Connecting to " + target + "....")
# Connecting to target ssid
wireless = Wireless()
wireless.connect(ssid=target, password=passw)
print("Connected")
