from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

CHROME_PATH = r"C:\Users\duart\Desktop\Code\chromedriver.exe"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfcdvgqGuK_cx2DZjQytULKEf6WHKWwR8Rrb6B-m9wnJymEiw/viewform?usp=sf_link"
LOCATION = "all midtown"
MAX_PRICE = 3000


class ApartmentHuntBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)  # USE PATH TO WHERE YOUR DRIVER IS LOCATED #
        self.location = LOCATION
        self.price = MAX_PRICE
        self.actions = TouchActions(self.driver)
        self.keys = Keys()

    def search_input(self):
        """use driver to input data for search purposes"""
        self.driver.get("https://streeteasy.com/")
        try:
            rental_button = self.driver.find_element_by_tag_name('Rentals')

        except NoSuchElementException:
            sleep(2)
            self.captcha()

        else:
            sleep(5)
            # rental button #
            rental_button.click()
            # location #
            neighborhood = self.driver.find_element_by_id("search-areas-dropdown-input")
            neighborhood.click()
            neighborhood.send_keys("All Midtown")
            self.driver.find_element_by_xpath('//*[@id="application"]').click()

            # close pop up #
            sleep(2)
            try:
                self.driver.find_element_by_xpath('//*[@id="content"]/main/section[1]/div/form/div[1]/div/div[3]'
                                                  '/div/div/div[1]/div[2]/button').click()

            except NoSuchElementException:
                pass

            else:
                # price - giving it only a maximum range, not minimum (price selected $3k) #
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="price_to"]/option[24]').click()

                # number of rooms #
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="content"]/main/section[1]/'
                                                  'div/form/div[1]/div/div[3]/fieldset/div/label[3]/span').click()

                # advanced options button #
                try:
                    sleep(2)
                    self.driver.find_element_by_css_selector("button.Home-advancedSearchLink").click()

                except NoSuchElementException:
                    pass

                else:
                    # amenities search (doorman and dog) #
                    sleep(2)
                    self.driver.find_element_by_name("amenities[doorman]").click()
                    sleep(2)
                    self.driver.find_element_by_name("amenities[pets]").click()

                    # click the search button #
                    try:
                        sleep(3)
                        search_button = self.driver.find_element_by_xpath('//*[@id="content"]/main/section[1]/div/'
                                                                          'form/div[1]'
                                                                          '/div/div[4]/button')
                        search_button.click()

                    except ElementClickInterceptedException:
                        sleep(2)
                        self.driver.find_element_by_xpath('//*[@id="content"]/main/section[1]/div/'
                                                          'form/div[1]/div/div[4]'
                                                          '/button').click()

    def get_search_results(self):
        """retrieve search results from website"""
        sleep(10)
        pass

    def captcha(self):
        """function used to bypass the website captcha"""
        sleep(3)
        captcha = self.driver.find_element_by_xpath('/html/body/div/iframe[0]')
        self.driver.switch_to.frame(captcha)
        captcha_loc = captcha.location
        print(captcha_loc)
        captcha_x = captcha_loc["x"]
        captcha_y = captcha_loc["y"]
        self.actions.tap_and_hold(captcha_x, captcha_y)
        sleep(5)
        self.actions.release(captcha_x, captcha_y)
        self.search_input()


bot = ApartmentHuntBot()

bot.search_input()
sleep(5)

bot.driver.quit()