#!/usr/share/python
# i'm still working on it to be more accurate.
# if u have a better solution please commit :) 
import socket, sys

import subprocess
import os

import nmap

ip = raw_input("Target IP: ")
nm = nmap.PortScanner()
machine = nm.scan(ip,arguments='-O')
print machine['scan'][ip]['osmatch'][0]['osclass'][0]['osfamily']
