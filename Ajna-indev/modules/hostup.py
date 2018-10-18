import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input("Target IP : ")
rep = os.system("ping -c 1 " + server_ip)

print ""
if rep == 0:
    
    print "[+] Server is up!"
else:
    
    print "[-] Server is down!"

