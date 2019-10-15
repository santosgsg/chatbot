import time

from selenium import webdriver
import os

class driver:
    def __init__(self):

        self.webdriver = webdriver.Chrome(chrome_options=self.configure())

    def configure(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
        options.add_argument('--headless')
        return options

    def search_img(self):
        self.webdriver.get('https://web.whatsapp.com')
        data = self.webdriver.find_element_by_xpath('//*[@class="_1pw2F"]/img').get_attribute('src')
        return data

    def check_notification(self):
        new = self.webdriver.find_elements_by_class_name('P6z4j')

        if (len(new) > 1):
            return True
        else:
            return False
        #  _1ZMSM de fora
        #  P6z4j de dentro

    def give_welcome(self):
        # continuar
        pass