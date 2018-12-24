import sys
import os
#from subprocess import call


from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def main():
	screen()
	print ""
	print "AJNA is a Security Scanner!"
	print "       Version: a0.81"
	print "           Made By: Vernieri\r\n"

	print "--------------{0}--------------"
	print "==============================="
	print "|      WHAT U WANNA DO?       |"
	print "|                             |"
	print "|1. Host Discovery(Single)    |"
	print "|2. Network Discovery(All)    |"
	print "|3. Port Scanner              |"
	print "|4. OS Detection(indev)       |"
	print "|5. Service Scanner(indev)    |"
	print "|9. Exit                      |"
	print "===============================\r\n"
	options = {1 : hostup,
			2 : netup,
			3 : portscan,
			4 : systemdt,
			5 : whois,
			9 : exit,

	}
	num = input("> ")
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
	os.system('python modules/osdetec-dev.py')

def netup():
	os.system('python modules/netup.py')

def hostup():
	os.system('python modules/hostup.py') 

main()

#Gratz Vernieri
