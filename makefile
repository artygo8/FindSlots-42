all: run

env:
	python3 -m pip install MechanicalSoup
	python3 -m pip install beautifulsoup4

run:
	@python3 main.py

hide:
	@python3 main.py & disown

