import requests
import os
from dotenv import load_dotenv

load_dotenv()

sheety_endpoint = "https://api.sheety.co"
username = "37230705c32a2318d2733fd64efefc08"
project_name = "flightPrices"
sheet_name = "sheet1"

token = os.getenv("sheety_token")

sheety_headers = {
    "Authorization": f"Bearer {token}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet

    def __init__(self):
        self.prices_endpoint = f"{sheety_endpoint}/{username}/{project_name}/sheet1"
        self.users_endpoint = f"{sheety_endpoint}/{username}/{project_name}/users"

    def get_sheet_data(self):
        response = requests.get(url=self.prices_endpoint, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        return data
    
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        return data
        

