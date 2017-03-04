from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import json


class FaceBlaster:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--force-device-scale-factor=1")
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://messenger.com")
        raw_input("Login to Messenger, then hit enter to continue ")

    def close(self):
        self.driver.close()

    def get_userids_from_post(self):
        driver = self.driver
        driver.get("https://facebook.com")
        raw_input("Login to FB, then hit enter to continue ")
        print "1. Navigate to your post"
        print "2. Click on the reactions (this should open a list of people)"
        print "3. If there are many reactions, scroll and 'see more' until the list has fully loaded."
        raw_input("4. Then, hit enter to continue ")
        ids = set()
        ul = driver.find_elements_by_xpath(
                '//ul[contains(@id, "reaction_profile_browser")]//a[contains(@data-hovercard, "/ajax/hovercard/user")]'
                )
        for li in ul:
            id_ = li.get_attribute("data-hovercard").split("id=")[1].split("&")[0]
            ids.add(id_)
        return list(ids)
    
    def send_message(self, contactid, custom_message):
        driver = self.driver
        driver.get("https://www.messenger.com/t/" + contactid)
        full_name = driver.find_element_by_xpath(
                '//div[@data-testid="info_panel"]//span'
                ).text.split()
        custom_message = custom_message.format(f_name = full_name[0])
        while True:
            print "Please enter 1, 2, or 3, and then hit enter:"
            print "   1. '{}'".format(custom_message)
            print "   2. Use a manually entered message"
            print "   3. Skip this person"
            r = raw_input("Your choice: ")
            if r in ["1", "2", "3", "4"]:
                break
            else:
                print "That was not a valid option"
                time.sleep(1)
        if r == "1":
            message = custom_message
        elif r == "2":
            print "Type your message here, then hit enter:"
            message = raw_input("Your message: ")
        elif r == "3":
            return "Skip"
        driver.find_element_by_xpath(
                '//div[@aria-label="Type a message..."]'
                ).send_keys(message)
        driver.find_element_by_xpath(
                '//div[@aria-label="Type a message..."]'
                ).send_keys(Keys.ENTER)
        return "Message sent"


if __name__ == '__main__':
    print "ctrl+c at any time to exit"
    F = FaceBlaster()
    contacts = F.get_userids_from_post()
    for contact in contacts:
        print F.send_message(
            contact,
            "{f_name}, please ignore this bot message."
            )
    F.close()
