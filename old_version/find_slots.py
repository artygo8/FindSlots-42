import os, time, chime, getpass
from bs4 import BeautifulSoup
import mechanicalsoup

chime.theme("big-sur") # ['big-sur', 'chime', 'mario', 'material', 'zelda']
VERBOSE = 1

print("\033[32;1mThis script is mostly not from me, it is based on https://github.com/artainmo/find_slots.\033[m")

#  _                   _       
# (_)_ __  _ __  _   _| |_ ___ 
# | | '_ \| '_ \| | | | __/ __|
# | | | | | |_) | |_| | |_\__ \
# |_|_| |_| .__/ \__,_|\__|___/
#         |_|                  


login = input("login: ")
password = getpass.getpass("password: ")
link = "https://projects.intra.42.fr/projects/cpp-module-07/slots?team_id=3421253"

if not link:
    link = input("link: ")

if not "https://projects.intra.42.fr/projects/" in link:
    chime.error()
    exit("Error: wrong link")


#  _             _       
# | | ___   __ _(_)_ __  
# | |/ _ \ / _` | | '_ \ 
# | | (_) | (_| | | | | |
# |_|\___/ \__, |_|_| |_|
#          |___/         


browser = mechanicalsoup.Browser()
try:
    login_page = browser.get(link) #We get redirected towards login page
except:
    chime.error()
    exit("no internet access !")
html_parser = login_page.soup

form = html_parser.select("form")[0]
form.select("input")[2]["value"] = login
form.select("input")[3]["value"] = password

new_page = browser.submit(form, login_page.url)
if login_page.url == new_page.url:
    chime.error()
    exit("Error: login or password")


#   __ _           _       _       _       
#  / _(_)_ __   __| |  ___| | ___ | |_ ___ 
# | |_| | '_ \ / _` | / __| |/ _ \| __/ __|
# |  _| | | | | (_| | \__ \ | (_) | |_\__ \
# |_| |_|_| |_|\__,_| |___/_|\___/ \__|___/
#                                          


def find_slot(tag):
    return tag.has_attr("data-full")

while 1:
    try:
        refresh = browser.get(new_page.url)
        # with open("refresh.html", "w+") as f: f.writelines(str(refresh.content.decode('UTF-8')))
        slot = refresh.soup.find_all(find_slot)
    except:
        chime.error()
        exit()

    if VERBOSE: print(len(refresh.content), end=" ", flush=True)

    if slot != []:
        chime.success()
        os.system("open " + new_page.url)
        break
    time.sleep(30)
