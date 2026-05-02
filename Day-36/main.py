STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

stock_api = ""
news_api = ""

import requests
from twilio.rest import Client

stock_api = ""
news_api = ""

twilio_sid = ""
twilio_auth = ""






stock_parameters = {
    "function": "TIME_SERIES_DAILY" ,
    "symbol": STOCK ,
    "apikey": stock_api ,

}



response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
day_list = list(stock_data["Time Series (Daily)"].keys())
yesterday = str(day_list[0])
the_day_before = str(day_list[1])
yesterday_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
the_day_before_close = float(stock_data["Time Series (Daily)"][the_day_before]["4. close"])
difference = yesterday_close - the_day_before_close
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_change = round((difference/the_day_before_close) * 100)
news_parameters = {
    "q" : COMPANY_NAME,
    "sortBy" : "popularity",
    "apiKey" : news_api,

}
if abs(percentage_change) >= 5:
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK}: {up_down}{percentage_change}%\nHeadlines: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]
    

    client = Client(twilio_sid, twilio_auth)

    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_="#virtual_trial_num_from_twilio",
            to="#actual_number"

        )

