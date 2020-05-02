import time
from selenium import webdriver
import selenium

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

    def go_to_profile(self):
        self.driver.get('http://www.instagram.com' + "\\" + self.username)
        time.sleep(2)

    def shutdown(self, delay=5):
        time.sleep(delay)
        self.driver.quit()

    def get_follower_ratio(self):
        # Only available on a profile page
        basic_info = self.driver.find_elements_by_class_name("g47SY")
        quick_info = []
        for element in basic_info:
            # getting the text value of each element and turning it into a integer
            element_value = element.get_attribute('innerHTML')
            element_value = int(element_value)
            quick_info.append(element_value)
        num_posts = quick_info[0]
        num_followers = quick_info[1]
        num_following = quick_info[2]
        follower_ratio = round(num_followers/num_following, 5)
        quick_info.append(follower_ratio)
        print(quick_info)
        return follower_ratio

    def check_private(self):
        # try except block to check if the word private appears in the appropriate box on a
        try:
            account_private = self.driver.find_element_by_class_name("rkEop")
            account_private_text = account_private.get_attribute("innerHTML")
            print(account_private_text)
            contains_private = "Private" in account_private_text
            print(contains_private)
            if contains_private:
                print("The account {} is private". format(self.username))
            else:
                print("Mistakes were made")
            return contains_private
        except selenium.common.exceptions.NoSuchElementException:
            print("The account {} is not private".format(self.username))
            return False

    def quick_analysis(self):
        self.go_to_profile()
        self.get_follower_ratio()


