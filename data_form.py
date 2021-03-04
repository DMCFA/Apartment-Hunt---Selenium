import os
from selenium import webdriver

FORM = os.environ.get("FORM_LINK") # form link goes here
CHROME_PATH = os.environ.get("file_path") # local path to the chrome driver app


class DataForm:

    def __init__(self):
        self.form = FORM # USE LINK TO YOUR GOOGLE (OR OTHER PARTY) FORM #
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)  # USE PATH TO WHERE YOUR DRIVER IS LOCATED #

    def send_data(self):
        pass