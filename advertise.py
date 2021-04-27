#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scapy.all import *
import time
import os

hostip = os.environ['HOST_IP']
destip = os.environ['DEST_IP']

print("Container started")
while True:
	send(IP(src=hostip, dst=destip)/ICMP())
	print("Sent from", hostip, "to", destip,"sleep 2.5 mins")
	time.sleep(150)