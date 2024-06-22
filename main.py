import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "NIW17EWLXNCHXVI6"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = "46727271080d49d6a4172c9a5fb6e569"\

TWILLIO_SID = "AC740ac3be0bfb5b8588b9e8c18f655b99"
TWILLIO_TOKEN = "3534759cccd171ece8b8c5a470ea8e25"





stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

stock_requests = requests.get(STOCK_ENDPOINT, params=stock_param)

stock_data = stock_requests.json()

yesterday_stock = stock_data["Time Series (Daily)"]

data_list = [value for (key, value) in yesterday_stock.items()]

yesterday_closing_price = float(data_list[0]["4. close"])



day_before_yest_closing_price = float(data_list[1]["4. close"])



stock_price_diff = (yesterday_closing_price - day_before_yest_closing_price)

up_down = None

if stock_price_diff > 0:
    up_down = "📈"
else:
    up_down = "📉"


stock_price_diff_percentage = round((stock_price_diff/day_before_yest_closing_price)*100, 2)

print(f"Stock Difference {stock_price_diff_percentage}%")

if stock_price_diff_percentage > 0.5:
    news_parameters = {
    "qIntitle": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API
}
    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    three_news_articles = news_response.json()["articles"][:3]
    news = [f"Headline: {article['title']}.\n\nBrief: {article['description']}" for article in three_news_articles]

    client = Client(TWILLIO_SID, TWILLIO_TOKEN)

    for article in news:
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {up_down} {stock_price_diff_percentage}%\n\n{article}",
            from_="+15188686356",
            to="+917044120323",
        )

        print("SMS Sent")
