#!/usr/share/python
import socket, sys
import threading
import subprocess
import os
import time

ip = raw_input("Your IP: ")
ip.split(".")
a,b,c,d = ip.split(".")

#nip = a+"."+b+"."+c+"."+"d"
#print nip

#print ""
#print "Scanning all the network, it may take a while..."
#print "Active routers will be printed below:"

def net1():
        with open(os.devnull, "wb") as limbo:
                for n in xrange(0, 63):

                        #ip="192.168.15.{0}".format(n)
                        nip = a+"."+b+"."+c+"."+"{0}".format(n) 
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", nip], stdout=limbo, stderr=limbo).wait()
                        time.sleep(0.2)
                        if result:
                                pass
                                #print "[-] ", nip, "is inactive"
                                #print "\r\n"
                        else:
                                print "[+] ", nip, "is active!"
                                
        #print "[!] Done!"
        
def net2():
        with open(os.devnull, "wb") as limbo:
                for n in xrange(64, 127):

                        #ip="192.168.15.{0}".format(n)
                        nip = a+"."+b+"."+c+"."+"{0}".format(n) 
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", nip], stdout=limbo, stderr=limbo).wait()
                        time.sleep(0.2)
                        if result:
                                pass
                                #print "[-] ", nip, "is inactive"
                                #print "\r\n"
                        else:
                                print "[+] ", nip, "is active!"
                                
        #print "[!] Done!"        

def net3():
        with open(os.devnull, "wb") as limbo:
                for n in xrange(128, 191):

                        #ip="192.168.15.{0}".format(n)
                        nip = a+"."+b+"."+c+"."+"{0}".format(n) 
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", nip], stdout=limbo, stderr=limbo).wait()
                        time.sleep(0.2)
                        if result:
                                pass
                                #print "[-] ", nip, "is inactive"
                                #print "\r\n"
                        else:
                                print "[+] ", nip, "is active!"
                                
        #print "[!] Done!"        

def net4():
        with open(os.devnull, "wb") as limbo:
                for n in xrange(192, 255):

                        #ip="192.168.15.{0}".format(n)
                        nip = a+"."+b+"."+c+"."+"{0}".format(n) 
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", nip], stdout=limbo, stderr=limbo).wait()
                        time.sleep(0.2)
                        if result:
                                pass
                                #print "[-] ", nip, "is inactive"
                                #print "\r\n"
                        else:
                                print "[+] ", nip, "is active!"
                                
        #print "[!] Done!"        

def main():
        t = time.time()

        t1 = threading.Thread(target=net1)
        t2 = threading.Thread(target=net2)
        t3 = threading.Thread(target=net3)
        t4 = threading.Thread(target=net4)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join() 
        t3.join()
        t4.join()     
        print "[+] Done!"  

main()         
