import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input("Enter server IP : ")
rep = os.system("ping " + server_ip)

if rep == 0:
    print "server is up"
else:
    print "server is down"

