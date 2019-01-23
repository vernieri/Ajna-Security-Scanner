#!/usr/bin/env python
import nmap # import nmap.py module
nm = nmap.PortScanner() # instantiate nmap.PortScanner object

ip = raw_input("Target IP: ")
port = raw_input("Port or range of ports: ")
nm.scan(ip, port) # scan host 127.0.0.1, ports from 22 to 443
print('----------------------------------------------------')
# print result as CSV
print(nm.csv())
