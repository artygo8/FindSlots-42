GRN_PRINTF () {
    printf "\033[32m$1\e[m\n"
}

RED_PRINTF () {
    printf "\033[0;31m$1\e[m\n"
}

python3.9 --version &>/dev/null
if [ $? -ne 0 ]; then
    RED_PRINTF "install python3.9 before continuing"
    exit
else
    GRN_PRINTF "python3.9 already installed"
fi

brew --version &>/dev/null
if [ $? -ne 0 ]; then
    RED_PRINTF "install homebrew before continuing"
    exit
else
    GRN_PRINTF "homebrew already installed"
fi

#Install chime
@python3.9 -c "import chime" &>/dev/null
if [ $? -ne 0 ]; then
    GRN_PRINTF "installing chime..."
    python3.9 -m pip install chime &>/dev/null
else
    GRN_PRINTF "chime already installed"
fi

#Install selenium
@python3.9 -c "import selenium" &>/dev/null
if [ $? -ne 0 ]; then
    GRN_PRINTF "installing selenium..."
    python3.9 -m pip install selenium &>/dev/null
else
    GRN_PRINTF "selenium already installed"
fi

# Install dotenv
@python3.9 -c "import dotenv" &>/dev/null
if [ $? -ne 0 ]; then
    GRN_PRINTF "installing dotenv..."
    python3.9 -m pip install python-dotenv &>/dev/null
else
    GRN_PRINTF "dotenv already installed"
fi

#Install geckodriver
ls /usr/local/Cellar/geckodriver &>/dev/null
if [ $? -ne 0 ]; then
    GRN_PRINTF "installing geckodriver..."
    brew install geckodriver &>/dev/null
else
    GRN_PRINTF "geckodriver already installed"
fi

#Install firefox
ls /Applications/Firefox.app &>/dev/null
if [ $? -ne 0 ]; then
    GRN_PRINTF "installing firefox..."
    brew install firefox &>/dev/null
else
    GRN_PRINTF "firefox already installed"
fi
