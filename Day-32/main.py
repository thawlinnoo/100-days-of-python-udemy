# import smtplib

# my_email = "tarocity66@gmail.com"
# password = "MY_PASSWORD"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() #encrypt the message if someone interrupt
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="tarocity66@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of the email")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday() #will print index in week
# print(year)

# data_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(data_of_birth)
# ------------------------------------

import random
import datetime as dt
import smtplib

with open("Day-32/quotes.txt", mode="r") as file:
    data = file.readlines()
data_list = [line.strip() for line in data]

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    my_email = "tarocity66@gmail.com"
    password = "MY_PASSWORD"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="thawlinnoo7@gmail.com",
            msg=f"Subject:Motivation quote\n\n{random.choice(data_list)}"
        )





