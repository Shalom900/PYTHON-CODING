import webbrowser
from colorama import *
import requests
from requests.auth import HTTPBasicAuth
import sys
import requests
from requests import *
import time
import colorama
from colorama import *
import pyfiglet
print(Fore.YELLOW+Style.BRIGHT)
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°".strip(""))
print(" Most deadliest spider specie by: Marven Hackers")
print("_____________________________________________________".strip(""))
text=":::::::::--)-)-}\nGiant\nSpider"
txt= ":::::::::--)-)-}"
banner= pyfiglet.figlet_format(text+"\n"+txt)
print(banner)
print("___________________________________________________")
print(" A Tool Created By:  Marven Hackers")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("\n")
print("\n")
print(Fore.RESET)
time.sleep(5)
import pyfiglet
print(Fore.YELLOW+Style.BRIGHT)
print("Choose the action you wanna take:")
print()
print()
x= "========> Exploit Any Website "
y= "=======> Scan Any Website with params "
u= "========> Hack Any Website"
j= "========> Join Our WhatsApp Group"
print("1.",x)
print()
print("2",y)
print()
print("3.",u)
print()
print("4.",j)
print()
pas="MarvelHacks"
while True:
 print(Fore.RED)
 user_p=input("Enter Tool Password First ====> ")
 print()
 print(Fore.RESET)
 print(Fore.GREEN+Style.BRIGHT)
 if user_p ==pas:
   print("Now Enter Any Of The Above Option")
   break
   continue
 elif user_p=="":
   print(Fore.YELLOW+Style.BRIGHT)
   print("""Using this tool is illegal
Contact Marven Hackers at +234-9113669828 For The Authorized Tool Password.""")
   print(Fore.RESET)
 else:
   print(Fore.YELLOW+Style.BRIGHT)
   print(f"{user_p} is wrong password...")
   print("Contact Marven Hackers At +234-9113669828 For The Authorize Tool Password.")
   print(Fore.RESET)
   print(Fore.GREEN+Style.BRIGHT)
   print()
 print("Choose the action you wanna take:")
 print()
 print()
 x= "========> Scrape Any Website "
 y= "=======> Scrape Any Website with params "
 u= "========> Hack Any Website"
 
 #j = "========> Join Our WhtatsApp Group"
 print("1.",x)
 print()
 print("2",y)
 print()
 print("3.",u)
 #print()
 #print("4.",j)
 print()
while True:
 user= input(": =========> ")
 print()
 if user =="q":
  break
  time.sleep(0.5)
 elif user =="1":
   time.sleep(1.5)
   print(Fore.YELLOW+Style.BRIGHT)
   text="Web "
   txt= "Scraper"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   print("Enter The Web URL You Wanna Scrape.")
   while True:
    user_t=input("=========> ")
    if user_t =="":
    	print("Enter A Valid Web Url")
    else:
    	break
   response= requests.get(f'{user_t}')
   print()
   for n in range(1,8):
   	time.sleep(3)
   	print(f"Attempting to penetrate --->  {user_t}")
   	print()
   	print(f"Retrieving data from ---> {user_t}")
   print(" Hacking in progress ==========> ",response.text)
   print()
   print()
   print(f"succesfully Scraped  {user_t} \n Check out the above messages for the web sensitive information.\n")
   print()
   print()
   print()
   print()
   time.sleep(18)
   print(Fore.YELLOW+Style.BRIGHT)
   text="Hackers "
   txt= "  Tool"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   print("1.",x)
   print()
   print("2",y)
   print()
   print("3.",u)
   print()
   print()   
   print("Choose Another Option For Another Attack.")
   print()
 elif user== "2":
   time.sleep(2)
   print("  User Id.")
   while True:
    user_i=input(" =========> ")
    if user_i =="":
    	print("Enter A Valid ID")
    else:
    	break
   print()
   print("  User Name")
   while True:
    user_n=input("=============> ")
    if user_n =="":
    	print("Enter User Name")
    else:
    	break
   time.sleep(1.5)
   print()
   payload=(f"id:{user_i},username:{user_n}")   
   print(Fore.YELLOW+Style.BRIGHT)
   text="Web "
   txt= "Scraper"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   print("  Enter Target Web URL")
   while True:
    user_u=input("  =============> ")
    if user_u =="":
    	print("Enter A Valid Web Url")
    else:
    	break
   time.sleep(1.5)
   resp=requests.get(f"{user_u}",params=payload)
   print()
   print()
   print()
   for j in range(1,7):
   	time.sleep(2.9)
   	print(f"Attempting to scrape ------> {user_u}")
   	print()
   	print(f"Crawling on ---------> {user_u}")
   print(" Hacking in progress ========> ",resp.text)
   print("response url=========> ",resp.url)
   print()
   print("successful!!!")
   print()
   print()
   print()
   time.sleep(18)
   print(Fore.YELLOW+Style.BRIGHT)
   text="Hackers "
   txt= "  Tool"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   print("1.",x)
   print()
   print("2",y)
   print()
   print("3.",u)
   print()
   print()  
   print("Choose Another Option For Another Attack.")
   print()
 elif user =="4":
   print(" Thanks For Your Love And  Support!!!")
   print()
   for t in range(1,5):
    time.sleep(1.3)
    print(" You are about to join Marven Hackers...")
    print("---------------------------------------------")
    print("Marven Hackers !")
    print("---------------------------------------------")
   time.sleep(1.1)
   wapp= "https://chat.whatsapp.com/GyYX27tm6zxA5C5lnMsW7b"
   webbrowser.open(wapp)
   time.sleep(1.8)
   print()
   print()
   print()
   print("===> Choose The Action You Wanna Take!")
   print()
   print("1.",x)
   print()
   print("2",y)
   print()
   print("3.",u)
   print()
   print("4.",j)
   print()
 elif user=="3":
   print(Fore.YELLOW+Style.BRIGHT)
   text="Hackers "
   txt= "  Tool"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   u_name= input("Enter your username  ------>: ")
   time.sleep(1)
   print()
   u_p= input("Enter your password ----->: ")
   print()
   time.sleep(1)
   t_web= input("Enter your target web link ------->: ")
   time.sleep(1)
   print()
   res=requests.get(t_web,auth= HTTPBasicAuth('{u_name}', '{u_p}'))
   time.sleep(1.2)
   for i in range(1,6):
    time.sleep(1.3)
    print(f"Hacking into ------>  {t_web}")
    print(f"Retrieving data from ------> {t_web}")
    time.sleep(5)
   print(res.text)
   print()
   print()
   print(f"Successufully retrieved data from {t_web}")
   print()
   time.sleep(18)
   print()   
   print(Fore.YELLOW+Style.BRIGHT)
   text="Hackers "
   txt= "  Tool"
   banner= pyfiglet.figlet_format(text+"\n" +txt)
   print(banner)
   print(Fore.RESET)
   print(Fore.GREEN)
   print("1.",x)
   print()
   print("2",y)
   print()
   print("3.",u)
   print()
   print()  
   print("Choose Another Option For Another Attack.")
   print()
 elif user =="":
   print(Fore.RED+Style.BRIGHT)
   print()
   print(" choose any of the above number.")
   print()
   time.sleep(1)
   print(Fore.RESET)
 else:
   print(Fore.RED+Style.BRIGHT)
   print()
   time.sleep(1.3)
   print(f" {user} is unsupported...\n Enter 'q' to exit")
   print()
   print(Fore.RESET)
   print(Fore.GREEN+Style.BRIGHT)
   print()
else:
  print(Fore.RED)
  print(f"{user_p} is unsuported\nContact Marven Hackers For Tool Password.")
  print(Fore.RESET)
  print(Fore.GREEN+Style.BRIGHT) 	