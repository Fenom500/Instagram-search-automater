import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import Hidden_info

service = Service(Hidden_info.path_to_chrome_webdriver)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.instagram.com')
time.sleep(30)



driver.quit()