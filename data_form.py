import os
from time import sleep
from selenium import webdriver
from search_manager import address, price, link

FORM = os.environ.get("FORM_LINK")  # form link goes here
CHROME_PATH = os.environ.get("file_path")  # local path to the chrome driver app
address_form = ""
price_form = ""
property_form = ""


class DataForm:

    def __init__(self):
        self.form = FORM  # USE LINK TO YOUR GOOGLE (OR OTHER PARTY) FORM #
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)  # USE PATH TO WHERE YOUR DRIVER IS LOCATED #

    def get_data_fields(self):
        """get the path for the different form fields and assign them to variables"""
        address_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]'
                                                         '/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
                                                         '/div/div[1]/input')
        price_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/'
                                                       'div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]'
                                                       '/div/div[1]/input')
        property_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/'
                                                          'div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
                                                          '/div/div[1]/input')

    def send_data(self):
        """write the data collected on the search manager class to the form"""
        sleep(5)
        while True:
            data = 1
            if len(address) > data:
                address_form.send_keys(address[data])
                price_form.send_keys(price[data])
                property_form.send_keys(link[data])
            else:
                break
            data += 1
