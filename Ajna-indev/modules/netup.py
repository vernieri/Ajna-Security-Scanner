#!/usr/share/python
import socket, sys

import subprocess
import os

ip = raw_input("Your IP: ")
ip.split(".")
a,b,c,d = ip.split(".")

#nip = a+"."+b+"."+c+"."+"d"
#print nip




with open(os.devnull, "wb") as limbo:
        for n in xrange(0, 255):

                #ip="192.168.15.{0}".format(n)
                nip = a+"."+b+"."+c+"."+"{0}".format(n) 
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", nip], stdout=limbo, stderr=limbo).wait()
                if result:
                        pass
                        #print "[-] ", nip, "is inactive"
                        #print "\r\n"
                else:
                        print "[+] ", nip, "is active!"
                        
print "[!] Done!"
