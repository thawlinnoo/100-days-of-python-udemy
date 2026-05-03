import requests
from datetime import datetime


username = "thaw"
token = "m1a2n3c4i5t6y7"
graph_id = "graph1"


pixel_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : token,
    "username" : username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{username}/graphs"

graph_config = {
    "id" : graph_id,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) 
# print(response.text)

post_pixel_endpoint = f"{pixel_endpoint}/{username}/graphs/{graph_id}"

today = datetime.now()


post_pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "15"
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)


put_pixel_endpoint = f"{pixel_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
put_pixel_config = {
    "quantity" : "4.5"
}

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixel_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)