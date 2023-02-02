import os
import colorama
from colorama import Fore, Style, init
import time
import urllib.request
import re

red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
dblue = Fore.BLUE
GREEN = Fore.GREEN
white = Fore.WHITE
colorama.init(autoreset=True)

banner = f"""

     ██▓███   ██░ ██  ██▓  ██████  ██░ ██                          
▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒                         
▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░                         
▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██                          
▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓                         
▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒                         
░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░                         
░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░                         
          ░  ░  ░ ░        ░   ░  ░  ░                         
                                                               
 ▄████▄   ▒█████    ██████ ▄▄▄█████▓ █    ██  ███▄ ▄███▓▓█████ 
▒██▀ ▀█  ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ██  ▓██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒▓█    ▄ ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▓██  ▒██░▓██    ▓██░▒███   
▒▓▓▄ ▄██▒▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▓▓█  ░██░▒██    ▒██ ▒▓█  ▄ 
▒ ▓███▀ ░░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒▒█████▓ ▒██▒   ░██▒░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░░▒░ ░ ░ ░  ░      ░ ░ ░  ░
░        ░ ░ ░ ▒  ░  ░  ░    ░       ░░░ ░ ░ ░      ░      ░   
░ ░          ░ ░        ░              ░            ░      ░  ░
░                                                                                                
"""
print(banner)
print("version 1.0 \nCreador - ZQYS\ ""\n\n\n")

# collect user input for url


def askforurl():
	global url
	website_is_up = ""
	longurl = input("Introduzca el URL que va querer que oculte ")
	print(Style.RESET_ALL)
	try:
		global status_code
		status_code = urllib.request.urlopen(longurl).getcode()
	except:
		print(f"\n{yellow}Este URL no existe o no estan en linea en internet\n")
		askforurl()

	else:
		website_is_up = status_code == 200

	if any(i in longurl for i in ('https://', 'http://', ' ')) == False or website_is_up == "Falso":
		print(Fore.RED + "\nNo es una URL válida (agregue \"https://\" o \"http://\" \n\si no lo ha hecho) O el host de URL no está en linea")
		print(Style.RESET_ALL)
		askforurl()
	else:
		print(Fore.GREEN + "\nURL Valido!")
		print(Style.RESET_ALL)
		global url
		url = longurl

askforurl()
#global keywords
#keywords = keywords

keywords = input("Ingrese las palabras clave [para agregar el final de la URL] (separe las palabras clave con \"-\" [solo 10 palabras:])")
		
def shortenurl2():
	print(Fore.GREEN + "\n\n-----------EXITOSO-----------")
	print(Style.RESET_ALL)
	result = os.popen('curl da.gd/s/?url=' + url).read()
	print("\nNueva URL oculta: " + result)

def shortenurl():
	global url
#global keywords
	print(Fore.GREEN + "\n\n-----------EXITOSO-----------")
	print(Style.RESET_ALL)
	newurl = os.popen('curl \"da.gd/s/?url=' + url + "&shorturl=" + keywords + "\"").read()
	print("\nNueva URL oculta: " + newurl)

askforkeywords = input(": ¿Quieres añadir palabras clave? (y/n)")
if askforkeywords == "y" :
    #shortenurl()
    print(f"\n{blue}[/]{GREEN}Ok vamos a la siguiente sección")
elif askforkeywords == "n":
		#shortenurl2()
    print(f"\n{blue}[/]{GREEN}Ok vamos a la siguiente sección")
else:
		print(Fore.RED + "\n\nEscribe \"y\" para si y \"n\" para no estan dificil" )
		print(Style.RESET_ALL)

q1 = input("¿Quieres esconderte más como un profesional? (y/n): ")

if q1 == "y":
    website = input("Ingrese la URL para enmascarar la URL de phishing 'ex [https://google.com, http://real.web.lk]' --->")
    sc = input("Ingrese palabras de ingeniería social\n[!] No use espacios use '-' entre palabras de ingeniería social\n --->")
    print( "Generando Link... \n")
    newurl = os.popen('curl \"da.gd/s/?url=' + url + "&shorturl=" + keywords + "\"").read()
    result = os.popen('curl da.gd/s/?url=' + url).read()
    result1 = newurl.replace('https://', '')
    result2 = result.replace('https://', '')
    print("\nAquí está el hideurl_1 avanzado ----> "+website+'-'+sc+"@"+result1)
    print("Aquí está el hideurl_2 avanzado ----> "+website+'-'+sc+"@"+result2)
    
elif q1 == "n":
	shortenurl2()
    
else:
		print(Fore.RED + "\n\nEscriba \"y\" para sí y \"n\" para no... no es tan difícil")
		print(Style.RESET_ALL)