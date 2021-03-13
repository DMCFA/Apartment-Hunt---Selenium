import os
from time import sleep
from selenium import webdriver
from search_manager import address, price, link

FORM = os.environ.get("FORM_LINK") # form link goes here
CHROME_PATH = os.environ.get("file_path") # local path to the chrome driver app
address_form = ""
price_form = ""
property_form = ""

class DataForm:

    def __init__(self):
        self.form = FORM # USE LINK TO YOUR GOOGLE (OR OTHER PARTY) FORM #
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)  # USE PATH TO WHERE YOUR DRIVER IS LOCATED #

    def get_data_fields(self):
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
        sleep(2)
        try: