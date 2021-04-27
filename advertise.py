#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scapy.all import *
import time
import os

hostip = os.environ['HOST_IP']

print("Container started")
while True:
	send(IP(src=hostip, dst="8.8.8.8")/ICMP())
	print("Sent from", hostip, "sleep 2.5 mins")
	time.sleep(150)