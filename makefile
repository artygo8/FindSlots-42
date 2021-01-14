GRN_PRINTF = printf "\033[32m%s\e[m\n"

all: run

env:
	@python3 -c "import chime" && ${GRN_PRINTF} "chime installed" || python3 -m pip install chime
	@python3 -c "import selenium" && ${GRN_PRINTF} "selenium installed" || python3 -m pip install selenium
	@python3 -c "import getpass" && ${GRN_PRINTF} "getpass installed" || python3 -m pip install getpass
	brew install geckodriver
	brew install firefox

run:
	@python3 find_slots_selenium.py


#Install brew on mac school
#https://gist.github.com/skyl/36563a5be809e54dc139

#Install python3 on mac school
#PATH=PATH=/Users/$USER/.brew/bin:/usr/local/bin:/usr/bin:/bin:/ -> write in .zshrc -> reopen new terminal
#Brew install python@3
#Verify with python3 --version
#You should have Python 3.9.1
