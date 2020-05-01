import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import Hidden_info


class IGBot:

    def __init__(self):
        # logs in to homepage
        # opens up instagram.com website and sets variables necessary
        self.login_username = Hidden_info.instagram_login_username
        self.password = Hidden_info.instagram_password
        self.username = Hidden_info.instagram_username
        self.driver = webdriver.Chrome(Hidden_info.path_to_chrome_webdriver)
        self.driver.get('http://www.instagram.com')
        time.sleep(3)

        # Inputs necessary keys and clicks login button
        self.username_field = self.driver.find_element_by_name("username")
        self.username_field.send_keys(self.login_username)

        self.password_field = self.driver.find_element_by_name("password")
        self.password_field.send_keys(self.password)
        time.sleep(1)

        self.submit_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        time.sleep(3)

        # closes out of notification request popup
        self.not_Now_Button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        time.sleep(1)

    def go_to_Profile(self):
        self.driver.get('http://www.instagram.com' + "\\" + self.username)
        time.sleep(2)

    def shutdown(self, delay=5):
        time.sleep(delay)
        self.driver.quit()


# Logging In:
User = IGBot()
User.go_to_Profile()

User.shutdown(delay=8)
