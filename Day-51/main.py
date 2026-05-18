import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

load_dotenv()


PROMISED_DOWN = int(os.getenv("PROMISED_DOWN"))
PROMISED_UP = int(os.getenv("PROMISED_UP"))
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

Speed_test_url = "https://fast.com/"
Twitter_url = "https://x.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)





class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(Speed_test_url)

        wait = WebDriverWait(self.driver, 90)

        Show_more_info_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more info")))
        Show_more_info_button.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#upload-value.succeeded")))

        self.down = self.driver.find_element(By.ID, value="speed-value" ).text

        self.up = self.driver.find_element(By.ID, value="upload-value").text


        if int(self.down) < PROMISED_DOWN or int(self.up) < PROMISED_UP:
            print(f"This is my current wifi speed.\nDownload: {self.down}\nUp:{self.up}\n\nIt is slower than the promised speed.\nDownload: {PROMISED_DOWN} \nUp: {PROMISED_UP}")






    def tweet_at_provider(self):
        
        self.driver.get(Twitter_url)

        wait = WebDriverWait(self.driver, 90)

        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/div/span/span')))
        sign_in_button.click()

        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "text")))
        email_input.send_keys(TWITTER_EMAIL)

        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Next']]")))
        next_button.click()

        # twitter security system treating me like a red flag cyber criminal and my bot cannot login... so i cannot continue...



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()

