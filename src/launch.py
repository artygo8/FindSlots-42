import os
import time
import sys
from bs4 import BeautifulSoup as bs #Lib used as HTML parser
import mechanicalsoup as ms #Used to interact with web pages like fill forms, creates headless (no graphical interface) browser, contains .soup object that refers to BeautifulSoup HTML-parser

def show_page(html_parser_bs):
    if isinstance(html_parser_bs, bs) == False:
        print("Error: show_page function arg")
        exit()
    print("-------------------HTML-------------------")
    print(html_parser_bs) #View text of html page
    print("-------------------TEXT-------------------")
    print(html_parser_bs.get_text().replace("\n\n\n", "")) #View text of html page
    print("-------------------END-------------------")

def find_slot(tag):
    if tag.has_attr("data-full"): #data-full is html tag that contains slot starting and ending time, if no slots exist it will not be found
        return True
    return False


login = sys.argv[1];
password = sys.argv[2];
link = sys.argv[3];

browser = ms.Browser()
login_page = browser.get(link) #We get redirected towards login page
html_parser = login_page.soup

form = html_parser.select("form")[0]
form.select("input")[2]["value"] = login
form.select("input")[3]["value"] = password

new_page = browser.submit(form, login_page.url)
if login_page.url == new_page.url:
    print("Error: login or password")
    exit()

slot = []
while slot == []:
    refresh = browser.get(new_page.url)
    slot = refresh.soup.find_all(find_slot)
    #print(slot)
    time.sleep(60)

os.system("open " + new_page.url)
