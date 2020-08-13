#!/usr/bin/python3

import os
import time
import sys, traceback
import ipaddress
import re

if os.getuid() != 0:
	print ("Sorry. This script requires sudo privledges")
	sys.exit()

def MainMenu():
	time.sleep(0)

	print('''\033[1;35m
:::'###:::'##::::'##'########:'#######:::'##::: ##'##::::'##:::'###:::'########::
::'## ##:::##:::: ##... ##..:'##.... ##:::###:: ##:###::'###::'## ##:::##.... ##:
:'##:. ##::##:::: ##::: ##::::##:::: ##:::####: ##:####'####:'##:. ##::##:::: ##:
'##:::. ##:##:::: ##::: ##::::##:::: ##:::## ## ##:## ### ##'##:::. ##:########::
 #########:##:::: ##::: ##::::##:::: ##:::##. ####:##. #: ##:#########:##.....:::
 ##.... ##:##:::: ##::: ##::::##:::: ##:::##:. ###:##:.:: ##:##.... ##:##::::::::
 ##:::: ##. #######:::: ##:::. #######::::##::. ##:##:::: ##:##:::: ##:##::::::::
..:::::..::.......:::::..:::::.......::::..::::..:..:::::..:..:::::..:..:::::::::\033[1;m
							\033[1;31m Creator: Jeevan Chandra''')				


	print('''\033[1;36m
Script granted ROOT# Privileges!

 1.Nmap Quick Scan
 2.Nmap Basic-Version Scan
 3.Nmap Aggressive Scan
 4.Nmap Port Scan
 5.Nmap All Port Scan
 6.Nmap Vuln Scan
 7.Nmap Recon Scan

	\033[1;m''')

	selection = int (input("Enter your choice from [1-9]: "))
	print('''


	''')	

	ipaddress = input("ENTER A VALID IP_ADDERSS: ")	
	
	print('''\033[1;32m

		Checking ping!!!!

	\033[1;m''')

	cmd = "ping -c 1 %s" %ipaddress
	response = os.system(cmd)
	
	if response == 0:
	
 		print('''\033[1;32m

		Hurrey! the host is up!
		
		\033[1;m''')
	elif response != 0:
	
		print('''\033[1;31m
	
		Seems like the host is down!

		\033[1;m''')
		
		print('''\033[1;32mCODE REGENERATION IN 5 SEC\033[1;m''')
		time.sleep(5)
		
		cmd= os.system("clear")
		MainMenu()
	
	time.sleep(3)


	if selection == 1:
		
		print('''\033[1;33m 
		|====Nmap Quick Scan====| 
		\033[1;m''')

		

		print("what to write the output to a file? (1/0)")
		print("1=Yes [or] 0=No")

		selection = int (input("Enter your choice: "))
		

		if selection == 1:
			cmd = "nmap -T5 --max-retries 1 --max-scan-delay 20 --defeat-rst-ratelimit --open -oN Nmap-Quick %s" %ipaddress
			os.system(cmd)
			print("Output written to [nmap-scan] ")

		elif selection == 0:
			cmd = "nmap -T5 --max-retries 1 --max-scan-delay 20 --defeat-rst-ratelimit --open %s" %ipaddress
			os.system(cmd)
		exit()
			
	elif selection == 2:
		
		print('''\033[1;33m 
		|====Nmap Version Scan====| 
		\033[1;m''')
		
		print("what to write the output to a file? (1/0)")
		print("1=Yes [or] 0=No")

		selection = int (input("Enter your choice: "))
		if selection == 1:
			cmd = "nmap -sCV -T5 -oN Basic %s" %ipaddress	
			os.system(cmd)
		elif selection == 0:
			cmd = "nmap -sCV -T5 %s" %ipaddress
			os.system(cmd)	
		exit()	

	elif selection == 3:
		
		print('''\033[1;33m 
		|====Nmap Aggressive Scan====| 
		\033[1;m''')

		print("what to write the output to a file? (1/0)")
		print("1=Yes [or] 0=No")

		selection = int (input("Enter your choice: "))
		if selection == 1:
			cmd = "nmap -sCV -A -T5 -oN Aggressive %s" %ipaddress	
			os.system(cmd)
		if selection == 0:
			cmd = "nmap -sCV -A -T5 %s" %ipaddress	
			os.system(cmd)
		exit()
		
	elif selection == 4:
		
		print('''\033[1;33m 
		|====Nmap Port Scan====| 
		\033[1;m''')
		
		
		port = input("Enter the port number range you want to scan:")
		cmd = "nmap -T5  -p {0} {1}".format(port, ipaddress)
		os.system(cmd)
		exit()

	elif selection == 5:
		
		print('''\033[1;33m 
		|====Nmap Full Scan====| 
		\033[1;m''')
		
		print("what to write the output to a file? (1/0)")
		print("1=Yes [or] 0=No")

		selection = int (input("Enter your choice: "))
		if selection == 1:
			cmd = "nmap -p- --max-retries 1 --max-rate 500 --max-scan-delay 20 -T5 -v -A -oN Full %s" %ipaddress	
			os.system(cmd)
		if selection == 0:
			cmd = "nmap -p- --max-retries 1 --max-rate 500 --max-scan-delay 20 -T5 -v -A %s" %ipaddress	
			os.system(cmd)
		exit()	

	elif selection == 6:
		
		print('''\033[1;33m 
		|====Nmap Vuln Scan====| 
		\033[1;m''')
		
		print("what to write the output to a file? (1/0)")
		print("1=Yes [or] 0=No")

		selection = int (input("Enter your choice: "))
		if selection == 1:
			cmd = "nmap -sV -T5 --max-retries 1 --max-rate 500 --script vuln -oN Vulns %s" %ipaddress	
			os.system(cmd)
		if selection == 0:
			cmd = "nmap -sV -T5 --max-retries 1 --max-rate 500 --script vuln %s" %ipaddress	
			os.system(cmd)
		exit()	
	
	elif selection == 7:
		
		print('''\033[1;33m 
		|====Running Recon Scan====|
		\033[1;m''')

		cmd1 = "nmap -T5 -Pn -sV -A  %s" %ipaddress
		cmd2 = "nmap -T5 -Pn --script vuln  %s" %ipaddress	
		cmd3 = "gobuster dir -u http://%s -w /usr/share/dirb/wordlists/common.txt" %ipaddress
		cmd4 = "nikto -h %s" %ipaddress 

		os.system(cmd1)
		os.system(cmd2)
		os.system(cmd3)
		os.system(cmd4)
		exit()
MainMenu()
