import requests
from datetime import datetime as dt
import smtplib
import time

MY_LAT = 13.668
MY_LONG = 100.633

def above_me():


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude-5<=MY_LAT<=iss_latitude+5 and iss_longitude-5<=MY_LONG<=iss_longitude+5:
        return True
    else:
        return False
    




def night_time():
    parameters = {
        "lat": MY_LAT,
        "lng" :MY_LONG,
        "formatted" : 0,
        "tzid" : "Asia/Bangkok" #currently show in utc so we gotta change time zone 
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) 
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) 

    now = dt.now().hour
    if now < sunrise or now > sunset:
        return True
    else :
        return False

while True:
    if night_time() and above_me():
        my_email = "tarocity66@gmail.com"
        password = "MY_PASSWORD"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="thawlinnoo7@gmail.com",
                msg="Subject:Hello\n\nLook Up.. ISS is above you now"

            )
        time.sleep(60)


