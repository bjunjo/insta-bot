import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = YOUR CHROM DRIVER PATH
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = YOUR INSTAGRAM USERNAME
PASSWORD = YOUR INSTAGRAM PASSWORD


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(f"https://www.instagram.com/accounts/login/")
        sleep(2)

    def login(self):
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(USERNAME)
        pwd = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(2)

        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        except NoSuchElementException:
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")


    def find_followers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        all_followers = int(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',',''))
        sleep(2)

        # Select the popup box and scroll popup down
        popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in follow_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            sleep(1)


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()

