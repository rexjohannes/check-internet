import requests
import time
from pythonping import ping
from colorama import init, Fore
init()

print(Fore.CYAN + "Methods: \n1 - Web Request\n2 - Ping Request")

a = input(Fore.BLUE + "Please select a Method: ")

if a == "":
    a = "2"
else:
    a = a

try:
    a = int(a)
except:
    print(Fore.RED + "Please insert a vaild Code!")
    exit()
    
c = input(Fore.BLUE + "Please enter a Cooldown: ")

if c == "":
    c = "1"
else:
    c = c

try:
    c = int(c)
except:
    print(Fore.RED + "Please insert an int!")
    exit()
    
if a == 1:
    b = input(Fore.BLUE + "Url: ")
    if b == "":
        url = "https://google.de"
    else:
        url = b
        print(Fore.YELLOW + "Starting...")
    while True:
        try:
            requests.get(url)
            print(Fore.GREEN + "Found Internet Connection")
        except:
            print(Fore.RED + "No Internet Connection")
        time.sleep(c)
        
if a == 2:
    b = input(Fore.BLUE + "IP: ")
    if b == "":
        ip = "8.8.8.8"
    else:
        ip = b
    print(Fore.YELLOW + "Starting Ping...")
    while True:
        ping(ip, verbose=True, count=1, size=32)
        time.sleep(c)
    
else:
    print(Fore.RED + "This is not a vaild Code!")
