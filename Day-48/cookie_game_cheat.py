from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)


language_choose = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language_choose.click()

time.sleep(2)

start_time = time.time()

while True:
    cookie_button = driver.find_element(By.ID, value="bigCookie")
    cookie_button.click()


    try:
        available_products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        highest_price = 0
        if len(available_products) != 0:
            best_product = None

            for product in available_products:
                price = product.find_element(By.CLASS_NAME, "price").text #drive is for the whole webpage, "use variable to search only in it"

                if price != "":
                    price_num = int(price.replace(",", ""))

                if price > highest_price:
                    highest_price = price
                    best_product = product

            

            best_product.click()
    except ValueError:
        continue

    current_time = time.time()

    if current_time-start_time>300:
        cookie_per_sec = driver.find_element(By.ID, value="cookiesPerSecond").text
        print(f"cookies/second : {cookie_per_sec.split()[-1]}")
        break


    

        
