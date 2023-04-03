import requests
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f33927f8fb25fd8a542159d17e2429b4"
weather_params = {
    "lat":50.521400,
    "lon":19.155270,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(OWM_endpoint, params=weather_params)
#print(response.status_code) di test per verificare 200
response.raise_for_status() #check se ha problemi
weather_data = response.json()
# with open( "prova.json", "w") as file:
#     file.write(str(weather_data))
weather_slice = weather_data["hourly"][:12]
print (weather_slice)
# print (weather_data["hourly"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        #print ("bring an umbrella") stampa troppe volte
        will_rain = True
if will_rain:
    print ("bring an umbrella")




