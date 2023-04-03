import requests
from twilio.rest import Client
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f33927f8fb25fd8a542159d17e2429b4"
weather_params = {
    "lat":50.521400,
    "lon":19.155270,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
TWILIO_ACCOUNT_SID = "AC90490eb4bde8f275476f7088706b0e2f"
TWILIO_AUTH_TOKEN = "43baaec2d8c5743ee30dcabad37470aa" 

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
response = requests.get(OWM_endpoint, params=weather_params)
#print(response.status_code) di test per verificare 200
response.raise_for_status() #check se ha problemi
weather_data = response.json()
# with open( "prova.json", "w") as file:
#     file.write(str(weather_data))
weather_slice = weather_data["hourly"][:12]
#print (weather_slice)
# print (weather_data["hourly"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        #print ("bring an umbrella") stampa troppe volte
        will_rain = True
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today Remember the umbrella.", 
            from_= '+15013226175',
            to='+39 331 360 8213'
        )
    print (message.status)




