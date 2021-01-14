from selenium import webdriver
import getpass, time, chime

class Intra42:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.my_url = "https://projects.intra.42.fr/projects/cpp-module-07/slots?team_id=3424654"
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
        return self.get_url() == self.my_url

    def is_slot_present(self):
        self.driver.refresh()
        time.sleep(5) # to be sure the load is done.
        return self.driver.find_element_by_class_name("fc-time-grid-event")


if __name__ == "__main__":

    intra = Intra42()

    while not intra.is_connected():
        print("You have 60 seconds to connect!")
        time.sleep(60)

    while 1:
        try:
            intra.is_slot_present()
            chime.success()
            print('!', end='', flush=True)
        except:
            print('.', end='', flush=True)
        time.sleep(40)
