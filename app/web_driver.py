import time

from selenium import webdriver
import os

from app.mensagens import Mensagem


class Driver:
    def __init__(self):
        self.webdriver = webdriver.Chrome(chrome_options=self.configure())

    def configure(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
        options.add_argument('--headless')
        return options

    def search_img(self):
        self.webdriver.get('https://web.whatsapp.com')
        time.sleep(2)
        data = self.webdriver.find_element_by_xpath('//*[@class="_1pw2F"]/img').get_attribute('src')
        return data

    def check_notification(self):
        new = self.webdriver.find_elements_by_class_name('P6z4j')
        return len(new)
        #  _1ZMSM de fora
        #  P6z4j de dentro

    def give_welcome(self, message):
        # continuar
        chat_list = self.webdriver.find_elements_by_class_name('X7YrQ')
        for chat in chat_list:
            content = chat.find_elements_by_class_name('P6z4j')
            if (content):
                chat.click()
                time.sleep(1)
                self.webdriver.find_element_by_class_name('_3u328').send_keys(message)

    def get_numbers(self):
        notifications = []
        for element in self.webdriver.find_elements_by_class_name('X7YrQ'):
            if element.find_elements_by_class_name('P6z4j'):
                notifications.append(element.find_element_by_class_name('_19RFN').text)

        return notifications