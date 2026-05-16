from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# num = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# num.click()

# num = driver.find_element(By.LINK_TEXT, value="276,240") # click by using link_text
# num.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Thaw Linn")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Linn Oo")

email = driver.find_element(By.NAME, value="email")
email.send_keys("thawlinnoo7@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
sign_up.click()