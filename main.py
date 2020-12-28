from urllib.request import urlopen
import time
import ssl
import sys
from getpass import getpass
from bs4 import BeautifulSoup as bs #Lib used as HTML parser
import mechanicalsoup as ms #Used to interact with web pages like fill forms, creates headless (no graphical interface) browser, contains .soup object that refers to BeautifulSoup HTML-parser
#ssl._create_default_https_context = ssl._create_unverified_context #bypass ssl certificates to avoid errors on 42intra

def find_slot(tag):
    if tag.has_attr("data-index-url"):
        return True
    return False

def show_page(html_parser_bs):
    if isinstance(html_parser_bs, bs) == False:
        print("Error: show_page function arg")
        exit()
    print("-------------------HTML-------------------")
    print(html_parser_bs) #View text of html page
    print("-------------------TEXT-------------------")
    print(html_parser_bs.get_text().replace("\n\n\n", "")) #View text of html page
    print("-------------------END-------------------")


if __name__ == "__main__":
    begin_link = "https://projects.intra.42.fr"
    if len(sys.argv) != 4:
        link = input("Link to find slot page: ")
        if link[0:38] != "https://projects.intra.42.fr/projects/":
            print("Error: wrong link")
            exit()
        login = input("Login: ")
        password = getpass()
    else:
        login = sys.argv[1]
        password = sys.argv[2]
        link = sys.argv[3]

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

    while True:
        refresh = browser.get(new_page.url)
        show_page(refresh.soup)#0 after Intra project slots equals to 0 notifications not slots I believe..
        data_index_url = refresh.soup.find_all(find_slot)[0]["data-index-url"]
        json_file_link = begin_link + data_index_url
        print(json_file_link)
        json = ms.Browser().get(json_file_link).json()
        print(json)
        exit()
        time.sleep(60)
