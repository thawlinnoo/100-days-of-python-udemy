import requests
from datetime import datetime
import os
from dotenv import load_dotenv


today = datetime.now()

load_dotenv()

serpapi_api_key = os.getenv("serpapi_api_key")
serpapi_endpoint = "https://serpapi.com/search.json"





class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.serpapi_api_key = serpapi_api_key


    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        serpapi_parameter = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.serpapi_api_key,
            "stops" : "0" if is_direct else "1",
            
            
        }
        response = requests.get(url=f"{serpapi_endpoint}", params=serpapi_parameter)
        # return response.text
        response.raise_for_status()
        data = response.json()
        return data

        
