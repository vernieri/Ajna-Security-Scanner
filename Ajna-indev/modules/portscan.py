#!/usr/bin/python
import socket
import threading
import time

# Working in a Multi-Thread Mode to optimize this...
# Maybe doing all this C++ will be better...i'm studying about it.

ip = raw_input("Target IP: ")

def portscan1():
	#ip = raw_input("Target IP: ")
	for port in range(1,32767):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((ip, port))==0:
			time.sleep(0.1)
			print "[+]",port," is Open!"
			s.close

def portscan2():
	#ip = raw_input("Target IP: ")
	for port in range(32768,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((ip, port))==0:
			time.sleep(0.1)
			print "[+]",port," is Open!"
			s.close					
def main():
    t = time.time()

    t1 = threading.Thread(target=portscan1)
    t2 = threading.Thread(target=portscan2)	

    t1.start()
    t2.start()   

    t1.join()
    t2.join()             
    print "[+] Done!"  

main()                 
