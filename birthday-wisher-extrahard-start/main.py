##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib

with open("birthday-wisher-extrahard-start/letter_templates/letter_1.txt", "r") as file:
    letter_1 = file.read()

with open("birthday-wisher-extrahard-start/letter_templates/letter_2.txt", "r") as file:
    letter_2 = file.read()

with open("birthday-wisher-extrahard-start/letter_templates/letter_3.txt", "r") as file:
    letter_3 = file.read()

letter_list = []
letter_list.append(letter_1)
letter_list.append(letter_2)
letter_list.append(letter_3)

my_email = "tarocity66@gmail.com"
password = "MY_PASSWORD"

now = dt.datetime.now()
day = now.day
month = now.month

birthday_data = pandas.read_csv("birthday-wisher-extrahard-start/birthdays.csv")

for index in range(len(birthday_data["day"])):
    if birthday_data["day"][index] == day and birthday_data["month"][index] == month:
        picked_letter = random.choice(letter_list)
        Final_birthday_letter = picked_letter.replace("[NAME]", birthday_data["name"][index])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user= my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_data["email"][index],
                msg=f"Subject:Happy Birthday!!\n\n{Final_birthday_letter}"
            )
        

        





