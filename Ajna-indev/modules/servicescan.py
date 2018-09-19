#!/usr/share/python
import socket, sys

# I AM STILL WORKING ON IT AND IT MAY NOT WORK FOR ALL SERVICES
ip = raw_input("Target IP: ")
port = input("Target Port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send("What's up\r\n")
resp = s.recv(1024)
print resp
