import smtplib
import os
from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv()

my_email = os.getenv("email")
app_password = os.getenv("app_password")

data_manager = DataManager()



class NotificationManager:
    #This class is responsible for sending email with the deal flight details.
    def send_email(self, message):


        customer_data = data_manager.get_customer_emails()["users"]
        customer_emails = [
            user["whatIsYourEmail?"]
            for user in customer_data
        ]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=customer_emails,
                msg=f"Subject:New Flight Discount\n\n{message}"
            )