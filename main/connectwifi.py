#!/usr/bin/env python2

import sys

target = sys.argv[0]
passw = sys.argv[1]

# print("Connecting to " + target + "....")
# Connecting to target ssid
wireless = Wireless()
wireless.connect(ssid=target, password=passw)
print("Connected")
