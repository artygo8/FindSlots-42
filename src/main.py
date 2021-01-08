import os
import sys
from getpass import getpass

if __name__ == "__main__":
    link = input("Link to find slot page: ")
    if link[0:38] != "https://projects.intra.42.fr/projects/":
        print("Error: wrong link")
        exit()
    login = input("Login: ")
    password = getpass()
    if len(sys.argv) == 2 and sys.argv[1] == "HIDE":
        os.system("python3 src/launch.py " + login + " " + password + " " + link + " & disown");
    else:
        os.system("python3 src/launch.py " + login + " " + password + " " + link);
