import os
import sys
import subprocess
print(" 1 -> CUPP\n 2 -> NMAP\n 3 -> Commix\n")
choice = int(input("\nEnter The Choice : "))
# CUPP
def cupp () :
    print("Entering CUPP .||.")
    os.system("cd cupp && python3 cupp.py -i")
    return "ThankYou"
# NMAP
def nmap () :
    print("Entering NMAP .||.")
    ip = raw_input("Enter The IP Address : ")
    print("""Choose The Scan Types . . .\n
    1 : Intense Scan\n
    2 : Intense Scan Plus UDP\n
    3 : Intense Scan , All TCP Ports\n
    4 : Intense Scan , No Ping\n
    5 : Ping Scan\n
    6 : Quick Scan\n
    7 : Quick Scan Plus\n
    8 : Quick Traceroute\n
    9 : Regular Scan\n
    10 : Slow Comprehensive Scan\n
    """)
    scanType = int(input("Enter Your Choice : "))
    if scanType == 1 :
        os.system("nmap -T4 -A -v "+ip)
    elif scanType == 2 :
        os.system("nmap -sS -sU -T4 -A -v "+ip)
    elif scanType == 3 :
        os.system("nmap -p 1-65535 -T4 -A -v "+ip)
    elif scanType == 4 :
        os.system("nmap -T4 -A -v -Pn "+ip)
    elif scanType == 5 :
        os.system("nmap -sn "+ip)
    elif scanType == 6 :
        os.system("nmap -T4 -F "+ip)
    elif scanType == 7 :
        os.system("nmap -sV -T4 -O -F --version-light "+ip)
    elif scanType == 8 :
        os.system("nmap -sn --traceroute "+ip)
    elif scanType == 9 :
        os.system("nmap "+ip)
    elif scanType == 10 :
        os.system('nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script ""default or (discovery and safe)"" '+ip)
    else :
        os.system("nmap -T4 -A -v "+ip)
    return "ThankYou"
# Commix
def commix () :
    print("""1 -> Regular Attack
2 -> Tor Specialized Attack
3 -> Fore SSL/HTTPS
4 -> Enumeration - All
5 -> Purge Attack
6 -> Mobile Emulation Attack
7 -> Wizard Interface
    """)
    attackType = int(input("Enter The Attack Choice : "))
    if attackType == 1 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url)
    if attackType == 2 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"tor")
    if attackType == 3 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"--force-ssl")
    if attackType == 4 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"--all")
    if attackType == 5 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"--purge")
    if attackType == 6 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"--mobile")
    if attackType == 7 :
        url = raw_input("Enter The Target URL : ")
        os.system("commix -u "+url +"--wizard")
    return "ThankYou"
# Choice Decide
if choice == 1 :
    cupp()
elif choice == 2 :
    nmap()
elif choice == 3 :
    commix()
