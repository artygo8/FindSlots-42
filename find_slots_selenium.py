from selenium import webdriver
import getpass, time, chime

SLOTS_URL=""

class Intra42:

    def __init__(self):
        self.my_url = SLOTS_URL or input("slots url: ")
        self.driver = webdriver.Firefox()
        self.login_url = "https://signin.intra.42.fr/users/sign_in"
        self.driver.get (self.my_url)

    def __del__(self):
        self.driver.close()

    def login(self):
        self.driver.find_element_by_id("user_login").send_keys(input("login: "))
        self.driver.find_element_by_id("user_password").send_keys(getpass.getpass("password: "))
        self.driver.find_element_by_name("commit").click()

    def get_url(self):
        return self.driver.current_url

    def is_connected(self):
        return self.get_url() != self.login_url

    def is_slot_present(self):
        self.driver.refresh()
        time.sleep(5) # to be sure the load is done.
        return self.driver.find_element_by_class_name("fc-time-grid-event")


if __name__ == "__main__":

    chime.theme("mario")
    intra = Intra42()

    while not intra.is_connected():
        print("You have 60 seconds to connect!")
        time.sleep(60)

    while intra.get_url()== intra.my_url:
        try:
            intra.is_slot_present()
            chime.success()
            print('!', end='', flush=True)
        except:
            print('.', end='', flush=True)
        time.sleep(30)

    print("You can't access to the page:", intra.my_url)
    chime.error()
