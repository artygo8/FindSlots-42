all: run

env:
	python3 -m pip install MechanicalSoup
	python3 -m pip install beautifulsoup4
	python3 -m pip install lxml

run:
	@python3 src/main.py

hide:
	@python3 src/main.py HIDE




#Install brew on mac school
#https://gist.github.com/skyl/36563a5be809e54dc139

#Install python3 on mac school
#PATH=PATH=/Users/$USER/.brew/bin:/usr/local/bin:/usr/bin:/bin:/ -> write in .zshrc -> reopen new terminal
#Brew install python@3
#Verify with python3 --version
#You should have Python 3.9.1
