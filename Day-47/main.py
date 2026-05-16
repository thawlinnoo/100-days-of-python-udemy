import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
import time

load_dotenv()

my_email = os.getenv("email")
app_password = os.getenv("app_password")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

run= True
while run:
    response = requests.get(url, headers=headers)
    amazon_webpage = response.text

    soup = BeautifulSoup(amazon_webpage, "html.parser")

    price_whole = soup.find(name="span", class_="a-price-whole").get_text()
    price_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
    price = (f"{price_whole}{price_fraction}")
    price_into_float = float(price.replace(",", ""))
    print(price_into_float)
    if price_into_float < 100:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="thawlinnoo7@gmail.com",
                msg=f"Subject:Discount!!\n\nThe cooker is now just {price_into_float}"
            )
    time.sleep(86400)



