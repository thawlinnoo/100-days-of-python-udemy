api_key = "api key"

import requests

parameters = {
    "lat" : 13.756331,
    "lon" : 100.501762,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()


umbrella_require = (1 if hours["weather"][0]["id"]<700 else 0 for hours in weather_data["list"])
if 1 in umbrella_require:
    print("take umbrella")
else:
    print("no need umbrella")

