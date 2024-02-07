import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USERNAME = "Enter your username"
PASSWORD = "Enter your passwords"
INSTA_PAGE = "Page name"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD, Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{INSTA_PAGE}/followers")

        time.sleep(8)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);",
                                       self.driver.find_element(By.CSS_SELECTOR, '._aano'))
            time.sleep(2)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
