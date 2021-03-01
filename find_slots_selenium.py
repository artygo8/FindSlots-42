from selenium import webdriver
import time, chime, signal


# you can change these
SLOTS_URL = ""          # if not set, will be asked as input.
REFRESH_RATE = 42       # in seconds, be reasonable, please...
TIME_TO_CONNECT = 42

CHIME_THEME = "zelda"   # mario, zelda, material, big-sur or chime


# do not change these !
LOGIN_URL = "https://signin.intra.42.fr/users/sign_in"


# Colors
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)

colored = lambda rgb, text : f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[38;2;255;255;255m"


class Intra42:

    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.get(LOGIN_URL)
        except:
            exit(colored(RED,"Failed to start the webdriver"))

    def __del__(self):
        self.driver.quit()

    def is_connected(self):
        try:
            return "slots" in self.driver.current_url
        except:
            exit(colored(RED,"browser closed"))

    def is_slot_present(self):
        try:
            self.driver.refresh()
        except:
            exit(colored(RED,"browser closed"))
        time.sleep(5) # to be sure that the page is well loaded.
        return self.driver.find_element_by_class_name("fc-time-grid-event")


def signal_handler(sig, frame):
    chime.error()
    exit(colored(BLUE, "\ngood-bye !"))


# MAIN

if __name__ == "__main__":

    chime.theme(CHIME_THEME)
    signal.signal(signal.SIGINT, signal_handler)
    chime.info()
    intra = Intra42()

    while not intra.is_connected():
        print(colored(GREEN,f"You have {TIME_TO_CONNECT} seconds to get to your slots page."))
        time.sleep(TIME_TO_CONNECT)

    print(colored(GREEN, "You can now hide the browser, but close it only when you are done..."))

    while intra.is_connected():
        try:
            intra.is_slot_present()
            chime.success()
            print(colored(GREEN,'!'), end='', flush=True)
        except:
            print('.', end='', flush=True)
        time.sleep(REFRESH_RATE)

    print(colored(RED,"\nCan't access to the slots page anymore."))
    chime.warning()


# old things
"""
def login(self):
    import getpass # we don't need that in the current program
    self.driver.find_element_by_id("user_login").send_keys(input("login: "))
    self.driver.find_element_by_id("user_password").send_keys(getpass.getpass("password: "))
    self.driver.find_element_by_name("commit").click()
"""