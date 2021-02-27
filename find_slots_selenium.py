from selenium import webdriver
import time, chime, signal


# you can change these
SLOTS_URL = ""          # if not set, will be asked as input.
REFRESH_RATE = 35       # in seconds, be reasonable, please...

# do not change these !
LOGIN_URL = "https://signin.intra.42.fr/users/sign_in"
CHIME_THEME = "mario"


# Colors
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)

colored = lambda rgb, text : f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[38;2;255;255;255m"


class Intra42:

    def __init__(self):
        self.driver_ready = False
        self.my_url = SLOTS_URL or input(colored(GREEN,"slots url (URL of the slot page for your project):\n"))
        self.login_url = LOGIN_URL
        self.driver = webdriver.Firefox()
        self.driver_ready = True
        self.driver.get(self.my_url)

    def __del__(self):
        if self.driver_ready:
            self.driver.quit()

    # def login(self):
    #     import getpass # we don't need that in the current program
    #     self.driver.find_element_by_id("user_login").send_keys(input("login: "))
    #     self.driver.find_element_by_id("user_password").send_keys(getpass.getpass("password: "))
    #     self.driver.find_element_by_name("commit").click()

    def get_url(self):
        return self.driver.current_url

    def is_connected(self):
        return self.get_url() != self.login_url

    def is_slot_present(self):
        self.driver.refresh()
        time.sleep(5) # to be sure the load is done.
        return self.driver.find_element_by_class_name("fc-time-grid-event")


if __name__ == "__main__":

    chime.theme(CHIME_THEME)

    def signal_handler(sig, frame):
        chime.error()
        exit(colored(BLUE, "\ngood-bye !"))

    signal.signal(signal.SIGINT, signal_handler)

    chime.info()
    intra = Intra42()

    while not intra.is_connected():
        print(colored(GREEN,"You have 60 seconds to connect."))
        time.sleep(60)

    print(colored(GREEN,"You can now hide the browser, but do not close it..."))

    while intra.get_url() == intra.my_url:
        try:
            intra.is_slot_present()
            chime.success()
            print(colored(GREEN,'!'), end='', flush=True)
        except:
            print('.', end='', flush=True)
        time.sleep(REFRESH_RATE)

    print("You can't access to the page:", intra.my_url)
    chime.warning()
