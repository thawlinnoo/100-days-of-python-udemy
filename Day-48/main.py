from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}{price_cents.text}")




# # driver.close()
# driver.quit()


# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[3]')
# print(bug_link.text)

# ---------------------------------------------

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

date_list = []
name_list = []

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for date in dates:
    date_list.append(date.get_attribute("datetime")[0:10])
print(date_list)

for name in names:
    name_list.append(name.text)
print(name_list)

event_dict = {}

for event in range(len(date_list)):
    event_dict[event] = {
        "time" : date_list[event],
        "name" : name_list[event]
    }

print(event_dict)




driver.quit()