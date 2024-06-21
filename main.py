import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "NIW17EWLXNCHXVI6"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = "46727271080d49d6a4172c9a5fb6e569"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}


news_parameters = {
    "qIntitle": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API
}

stock_requests = requests.get(STOCK_ENDPOINT, params=stock_param)

stock_data = stock_requests.json()

yesterday_stock = stock_data["Time Series (Daily)"]

data_list = [value for (key, value) in yesterday_stock.items()]

yesterday_closing_price = float(data_list[0]["4. close"])



day_before_yest_closing_price = float(data_list[1]["4. close"])



stock_price_diff = abs(yesterday_closing_price - day_before_yest_closing_price)


stock_price_diff_percentage = (stock_price_diff/day_before_yest_closing_price)*100

print(f"Stock Difference {stock_price_diff_percentage}%")

if stock_price_diff_percentage > 0.5:
    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_articles = news_response.json()["articles"][:4]
    news = [f"Headline: {article['title']}. \n\n Brief: {article['description']}" for article in news_articles]
    print(news)
    







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

