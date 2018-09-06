import sys
import os
#from subprocess import call


from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def main():
	screen()
	print "AJNA is a Security Scanner!"
	print "       Version: 0.1"
	print "           Made By: Vernieri\r\n"

	print "--------------{0}--------------"
	print "==============================="
	print "|      WHAT U WANNA DO?       |"
	print "|                             |"
	print "|1. PortScanner               |"
	print "|2. Service Scanner(dev)      |"
	print "|3. OS Detect(dev)            |"
	print "|4. Host check(dev)           |"
	print "|9. Exit                      |"
	print "===============================\r\n"
	options = {1 : portscan,
			2 : whois,
			3 : systemdt,
			4 : hostup,
			9 : exit,

	}
	num = input()
	options[num]()

def screen():
	cprint(figlet_format('AJNA', font='starwars'),
       'white', 'on_blue', attrs=['bold'])

def portscan():
	#os.system('cd modules')
	os.system('python modules/portscan.py')

	#call(["python", "portscan.py"])

def exit():
	print "Bye!"
	sys.exit()

def whois():
	os.system('python modules/servicescan.py')


def systemdt():
	print "[-] i'm still in dev..."

def hostup():
	print "[-] i'm still in dev..."


main()

#Gratz Vernieri
