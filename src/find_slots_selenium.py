from selenium import webdriver
import time, chime, signal
import smtplib, ssl
import os
from dotenv import load_dotenv

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

g_new_slot = [1, 0]

def send_email(receiver_email, subject, content, password):
    sender_email = "find.slot.42@hotmail.com"
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        server = smtplib.SMTP('smtp.office365.com', 587)
    except Exception as e:
        print("EMAIL SERVER CREATION FAILED")
        print(e)
        return 0
    try:
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        message = "".join((
                "From : %s\n" % sender_email,
                "To : %s\n" % receiver_email,
                "Subject : %s\n" % subject,
                "\n",
                content,
                "\r\n"))
        server.sendmail(sender_email, [receiver_email], message)
    except Exception as e:
        if e.smtp_error.decode("utf-8")[0:73] == "5.7.139 Authentication unsuccessful, the user credentials were incorrect.":
            print("Wrong password guess.")
        else:
            print("SENDING EMAIL FAILED")
            print(e)
        server.close()
        return 0
    server.close()
    return 1

def setup_email():
    success = 0
    load_dotenv()
    if os.getenv("e_pass") != None:
        if (input("Do you want to continue with past email settings? (y/n) : ") == "y"):
            return 1
    while not success:
        if (input("Do you want to be notified by email when a slot is found? (y/n) : ") != "y"):
            return 0
        receiver = input("What is your email address? ")
        password = input("Guess the password (Amsterdam campus + # + special number) : ").lower()
        success = send_email(receiver, "TEST", "Move this mail from spam to inbox to allow next emails in inbox to generate noctifications.", password)
        if success and input("We send you a test email. Please confirm you received it and moved it from spam to inbox. (y/n): ") != 'y':
            success = 0
    with open(".env", "w") as f:
        f.write("e_notif="+receiver+"\n")
        f.write("e_pass="+password+"\n")
    return 1


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
    mail = setup_email()

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
            if mail and g_new_slot[0]:
                send_email(os.getenv("e_notif"), "SLOT FOUND", "Slot was found!", os.getenv("e_pass"))
                g_new_slot[0] = 0
            g_new_slot[1] = 0
        except:
            print('.', end='', flush=True)
            g_new_slot[1] += 1
            if g_new_slot[1] > 10:
                g_new_slot[0] = 1
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
