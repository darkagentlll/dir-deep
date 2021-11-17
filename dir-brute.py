import requests 
from colorama import Fore,init
import os
os.system("cls")
init()

print(Fore.BLUE+'''
██████╗░██╗██████╗░░░░░░░██████╗░███████╗██████╗░██████╗░
██╔══██╗██║██╔══██╗░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║██║██████╔╝█████╗██║░░██║█████╗░░██████╔╝██████╔╝
██║░░██║██║██╔══██╗╚════╝██║░░██║██╔══╝░░██╔═══╝░██╔═══╝░
██████╔╝██║██║░░██║░░░░░░██████╔╝███████╗██║░░░░░██║░░░░░
╚═════╝░╚═╝╚═╝░░╚═╝░░░░░░╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░░░░''')
print(Fore.MAGENTA+" ♛ Crated by Darkagent♛")

url=input(Fore.RED+"\n Enter Url: ")
mylist=("""robots.txt
wp-content/uploads/2021/04/
wp-content/uploads/2020/04/
wp-content/uploads/2019/04/
search/
admin/log
admin/
login/
sitemap.xml
sitemap.xml2
config.php
wp-login.php
log.txt
update.php
INSTALL.pgsql.txt
user/login/
INSTALL.txt
profiles/
scripts/
LICENSE.txt
CHANGELOG.txt
themes/
inculdes/
misc/
user/logout/
user/register/
cron.php
filter/tips/
comment/reply/
xmlrcp.php
modules/
install.php
MAINTAINERS.txt
user/password/
node/add/
INSTALL.sqlite.txt
UPGRADE.txt
INSTALL.myql.txt
""").split()


for i in mylist :
    req=requests.get(url+"/"+i)
    if req.status_code==200:
        print(Fore.GREEN+"[+]"+Fore.WHITE+url+"/"+i)
    else:
        print(Fore.RED+"[!]"+Fore.YELLOW+url+"/"+i)
