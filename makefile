all: run

env:
	python3 -m pip install MechanicalSoup
	python3 -m pip install beautifulsoup4
	brew install zenity

run:
	@python3 main.py
