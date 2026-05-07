#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import requests_cache



requests_cache.install_cache(
    "flight_cache",
    expire_after=3600
)


today = datetime.now()
today = today.date()
tomorrow = str(today + timedelta(days=1))
six_months_from_today = str(today + timedelta(days=180))


data_manager = DataManager()


flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_sheet_data()["sheet1"]
for row in sheet_data:
    destination = row["iataCode"]
    search_data = flight_search.check_flight("BKK", destination, tomorrow, six_months_from_today, is_direct=True)
    cheapest_flight = find_cheapest_flight(search_data, six_months_from_today)

    if cheapest_flight.price == "N/A":
        search_data = flight_search.check_flight("BKK", destination, tomorrow, six_months_from_today, is_direct=False)
        cheapest_flight = find_cheapest_flight(search_data, six_months_from_today)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < row["lowestPrice"]:
        message = f"{row['city']} Deal!\nPrice: {cheapest_flight.price}\nRoute: {cheapest_flight.origin_airport}-->{destination}\nDate: {cheapest_flight.out_date}\nStops: {cheapest_flight.stops}"
        notification_manager.send_email(message=message)




