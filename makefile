GRN_PRINTF = printf "\033[32m%s\e[m\n"

all: run

env:
	@chmod +x src/env.sh
	@src/env.sh

run:
	@python3.9 src/find_slots_selenium.py


#Install brew on mac school
#https://gist.github.com/skyl/36563a5be809e54dc139

#Install python3 on mac school
#PATH=PATH=/Users/$USER/.brew/bin:/usr/local/bin:/usr/bin:/bin:/ -> write in .zshrc -> reopen new terminal
#Brew install python@3
#Verify with python3 --version
#You should have Python 3.9
