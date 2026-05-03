

import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
token = os.getenv("SHEETY_TOKEN")

today = datetime.now()


print(today.strftime("%H:%M:%S"))

nutrition_endpoint = "https://app.100daysofpython.dev"

nutrition_parameter = {
    "query" : input("Tell me what exercises you did: "),  
}

headers = {
    "x-app-id" : app_id,
    "x-app-key" : api_key
}

response = requests.post(url=f"{nutrition_endpoint}/v1/nutrition/natural/exercise", json=nutrition_parameter, headers=headers)
data = response.json()


sheety_endpoint = "https://api.sheety.co"
username = "37230705c32a2318d2733fd64efefc08"
project_name = "udemyWorkouts"
sheet_name = "sheet1"

sheety_parameter = {
    "sheet1": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.post(url=f"{sheety_endpoint}/{username}/{project_name}/{sheet_name}", json=sheety_parameter, headers=sheety_headers)

print(response.status_code)
print(response.text)