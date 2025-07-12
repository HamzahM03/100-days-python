import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

YESTERDAY = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
TODAY = datetime.now().strftime('%Y-%m-%d')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Stock Price API setup
STOCK_PRICE_API_KEY = os.getenv('STOCK_PRICE_API_KEY')
stock_api_param = {
    "apikey": STOCK_PRICE_API_KEY
}
# stock_data = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA", params=stock_api_param).json()["Time Series (Daily)"]
response = requests.get(
    url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA",
    params=stock_api_param
)
data = response.json()
print(data)  # 🔍 check what you're actually getting

# stock_data = data["Time Series (Daily)"]




#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# Get a list of all close prices
all_closing = [float(value["4. close"]) for key,value in stock_data.items()]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = all_closing[1]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(all_closing[1] - all_closing[2])
print(diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round(diff/day_before_yesterday*100,2)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff < 5:
    # News API setup
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    news_api_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "Tesla",
        "from": YESTERDAY,
        "to": TODAY,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3
    }

    response = requests.get(NEWS_ENDPOINT, params=news_api_params)
    news_data = response.json()
    articles = []
    print(news_data)

    if news_data.get("status") != "ok":
        print("Error from NewsAPI:", news_data.get("message"))
    else:
        articles = news_data.get("articles", [])
        if not articles:
            print("No news articles found.")
        else:
            first_three_articles = [f"\nHeadline: {article['title']}\nBrief: {article['description']}" for article in articles[:3]]
            print(first_three_articles)

    print(first_three_articles)



    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

