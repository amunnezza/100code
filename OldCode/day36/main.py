from numpy import diff
import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

TWILIO_ACCOUNT_SID = "AC90490eb4bde8f275476f7088706b0e2f"
TWILIO_AUTH_TOKEN = "43baaec2d8c5743ee30dcabad37470aa" 

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN 


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "3A0MPNQ1WZ0JMP72"
NEWS_APY_KEY = "620fa813443a4fa99090e9cd550ac10c"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME, 
    "apikey":API_KEY, 
}
response = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response.json()["Time Series (Daily)"]
#qui decide di fare una lista con i soli valori senza mettere la data
#lo fa perchè se lo lancio tra quattro giorni comunque la lista sara aggiornata con i valori 
#in posizione 0 del giorno prima, in posizione [1] per 2 giorni fa e cosi via che sono le cose 
#che mi servono
data_list = [value for (key,value)  in data.items()]
yesterday_value = data_list[0] 
yesterday_closing_price = yesterday_value["4. close"]
print (yesterday_value)
print (yesterday_closing_price)

# with open ("data.json", "w") as file:
#     file.write(str(data))


# 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print (day_before_yesterday_closing_price)

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) #VOGLIO IL VALORE ASSOULO
# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price))* 100
print (diff_percent)
# 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 0.8 :
    news_params = {
        "apiKey":NEWS_APY_KEY,
        "q":COMPANY_NAME,
        "language":"en",
        "searchIn":"title"
        
        
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        
    #TODO 9. - Send each article as a separate message via Twilio.
    
         message = client.messages \
        .create(
            body=article, 
            from_= '+15013226175',
            to='+39 331 360 8213'
        )
        
       
    



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

