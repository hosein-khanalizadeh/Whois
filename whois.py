#!/usr/bin/python

import os
import sys
import re
from ipwhois import IPWhois
from socket import gethostbyname , gethostbyaddr


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
cyan = '\033[36m'
reset = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

def banner():
    print(f"""{blue}

 **************************************************
 *                                                *
 * dP   dP   dP dP     dP   .88888.  dP .d88888b  *
 * 88   88   88 88     88  d8'   `8b 88 88.    "' *
 * 88  .8P  .8P 88aaaaa88a 88     88 88 `Y88888b. *
 * 88  d8'  d8' 88     88  88     88 88       `8b *
 * 88.d8P8.d8P  88     88  Y8.   .8P 88 d8'   .8P *
 * 8888' Y88'   dP     dP   `8888P'  dP  Y88888P  *
 *                                                *
 **************************************************

 author  : hosein khanalizadeh
 githube : https://www.github.com/hosein-khanalizadeh

{reset}""")

def whois(ip:str):
    try:
        info = IPWhois(gethostbyname(ip)).lookup_whois()
        for inf in info.keys():
            print(f'{green} {inf} : {info[inf]}{reset}')
    except:
        print(f'{red} [!] Connection Failed !{reset}')

def main():
    os.system('cls')
    banner()
    host = input(f'{yellow} host >>> {reset}')
    print()
    if (re.search(ip_regex, host)):
        addr = host
        name = gethostbyaddr(addr)
    elif host.startswith('http://'):
        name = host[7:]
        addr = gethostbyname(name)
    elif host.startswith('https://'):
        name = host[8:]
        addr = gethostbyname(name)
    else:
        try:
            name = host
            addr = gethostbyname(name)
        except:
            print(f'{red} [!] Host or Ip is Not True !{reset}')
            sys.exit()
    print(f'{cyan} name : {name}{reset}')
    print(f'{cyan} addr : {addr}{reset}')
    print()
    whois(addr)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
