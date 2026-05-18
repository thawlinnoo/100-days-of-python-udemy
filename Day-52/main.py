import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TARGET_ACC = os.getenv("TARGET_ACC")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        self.driver.get(INSTAGRAM_URL)
        wait = WebDriverWait(self.driver, 90)
        Log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'Log in')]]")))
        Log_in_button.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "_r_2_")))
        email_input.send_keys(EMAIL)

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "_r_5_")))
        password_input.send_keys(PASSWORD)

        Log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')))
        Log_in_button.click()

        # code = input("Instagram sent the otp code to your email. The time is 8 seconds. Fill here: ").strip()
        # print(f"code received {code}")
        # code_input = wait.until(EC.element_to_be_clickable((By.ID, "_r_b_")))
        # code_input.send_keys(code)

        # Continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_Kb"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div')))
        # Continue_button.click()



        


    def find_followers(self):
        wait = WebDriverWait(self.driver, 90)

        Search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]')))
        Search_button.click()

        Search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Search input"]')))
        Search_input.send_keys(TARGET_ACC)

        top_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/chefsteps/']")))
        top_result.click()

        followers = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[contains(., 'followers')]]")))
        followers.click()

    def follow(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        follow_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[.//*[text()='Follow']]")))
        print(f"Found {len(follow_buttons)} follow buttons")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
            except Exception as error:
                print(error)

        


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()