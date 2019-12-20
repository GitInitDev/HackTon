import os
import sys
print(" 1 -> NMAP\n 2 -> Metasploit\n 3 -> Any other fuck")
choice = int(input("\nEnter The Choice : "))
# NMAP
if choice == 1 :
    ip = str(input("Enter The IP Address : "))
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
        os.system("nmap -T4 -A -v %s",%(ip))
    elif scanType == 2 :
        os.system("nmap -sS -sU -T4 -A -v %s",%(ip))
    elif scanType == 3 :
        os.system("nmap -p 1-65535 -T4 -A -v %s",%(ip))
    elif scanType == 4 :
        os.system("nmap -T4 -A -v -Pn %s",%(ip))
    elif scanType == 5 :
        os.system("nmap -sn %s",%(ip))
    elif scanType == 6 :
        os.system("nmap -T4 -F %s",%(ip))
    elif scanType == 7 :
        os.system("nmap -sV -T4 -O -F --version-light %s",%(ip))
    elif scanType == 8 :
        os.system("nmap -sn --traceroute %s",%(ip))
    elif scanType == 9 :
        os.system("nmap %s",%(ip))
    elif scanType == 10 :
        os.system("nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script ""default or (discovery and safe)"" %s",%(ip))
