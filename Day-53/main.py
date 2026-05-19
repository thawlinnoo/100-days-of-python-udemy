
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd3qNqmLJLrqi1ABlcQzU1HMMLPQxXvIuCt4lLFvnNu7svjaw/viewform?usp=publish-editor"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_CLONE_URL)
soup = BeautifulSoup(response.text, "html.parser")


link_list = []
prices_list = []
addresses_list = []

links = soup.find_all(class_="property-card-link")
for link in links:
    link_list.append(link.get("href"))

prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
for price in prices:
    formatted_price = price.text.split("/")[0].split("+")[0]
    prices_list.append(formatted_price)

addresses = soup.find_all("address")
for address in addresses:
    if "|" in address.text.strip():
        formatted_address = address.text.split("|")[1].strip()
    else:
        formatted_address = address.text.strip()

    addresses_list.append(formatted_address)




    
for property in range(len(link_list)):
    driver.get(GOOGLE_FORM_URL)
    wait = WebDriverWait(driver, 90)
    address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i1 i4"]')))
    address_input.send_keys(addresses_list[property])
    price_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i6 i9"]')))
    price_input.send_keys(prices_list[property])
    link_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i11 i14"]')))
    link_input.send_keys(link_list[property])
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Submit"]')))
    submit_button.click()
    time.sleep(2)
    another_form_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://docs.google.com/forms/d/e/1FAIpQLSd3qNqmLJLrqi1ABlcQzU1HMMLPQxXvIuCt4lLFvnNu7svjaw/viewform?usp=form_confirm']")))
    another_form_button.click()



    
    

    














