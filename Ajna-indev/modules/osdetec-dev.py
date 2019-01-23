#!/usr/share/python
import socket, sys

import subprocess
import os

import nmap

ip = raw_input("Target IP: ")
nm = nmap.PortScanner()
machine = nm.scan(ip,arguments='-O')
print machine['scan'][ip]['osmatch'][0]['osclass'][0]['osfamily']

#Must be Run as Root.
