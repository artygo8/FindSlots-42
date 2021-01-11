GRN_PRINTF = printf "\033[32m%s\e[m\n"

all: run

env:
	@python3 -c "import mechanicalsoup" && ${GRN_PRINTF} "mechanicalsoup installed" || python3 -m pip install MechanicalSoup
	@python3 -c "from bs4 import BeautifulSoup" && ${GRN_PRINTF} "bs4 installed" || python3 -m pip install beautifulsoup4
	@python3 -c "import lxml" && ${GRN_PRINTF} "lxml installed" || python3 -m pip install lxml
	@python3 -c "import chime" && ${GRN_PRINTF} "chime installed" || python3 -m pip install chime

run:
	@python3 find_slots.py



#Install brew on mac school
#https://gist.github.com/skyl/36563a5be809e54dc139

#Install python3 on mac school
#PATH=PATH=/Users/$USER/.brew/bin:/usr/local/bin:/usr/bin:/bin:/ -> write in .zshrc -> reopen new terminal
#Brew install python@3
#Verify with python3 --version
#You should have Python 3.9.1
