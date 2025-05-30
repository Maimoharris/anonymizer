RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"
banner=f"""{YELLOW}
#  ██████╗ ██████╗  █████╗  ██████╗██╗   ██╗██╗      █████╗ {CYAN}
#  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║   ██║██║     ██╔══██╗
#  ██║  ██║██████╔╝███████║██║     ██║   ██║██║     ███████║ {GREEN}
#  ██║  ██║██╔══██╗██╔══██║██║     ██║   ██║██║     ██╔══██║    {YELLOW}
#  ██████╔╝██║  ██║██║  ██║╚██████╗╚██████╔╝███████╗██║  ██║
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ TOOLS {PURPLE}
#            Author:MAIMO HARRIS Contact:+237680226898        
{END}"""
print(banner)
from os import system
import subprocess
print("You Must Run this Tool as Root\n\n")

def anontools():
    checktor:str=system("tor --help | grep 'tor -f'").to_bytes()
    checktornet:str=system("tornet").bit_count()
    if checktor==b'\x00':
        if checktornet==7:
            system("pip install tornet")
        else:
            pass
    else:
        system('sudo apt install tor')
        system("pip install tornet")
    return True
def anon(time,count):
    action=system(f'tornet --interval {time} --count {count}')

if __name__=="__main__":
    time=''
    count=''
    while time!=int or count!=int:
        try:
            time=int(input("Enter the time interval in seconds to change IP>>"))
            count=int(input("Enter the numbers of IP Counts 0 for infinite IPs>>"))
            if anontools():
                anon(time,count)
        except ValueError:
            print("This Inputs Must be an Integer....")
        except KeyboardInterrupt:
            print('\n[+] Exiting Tool...')
            system("exit")

