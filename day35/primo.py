import requests
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f33927f8fb25fd8a542159d17e2429b4"
weather_params = {
    "lat":42.051781,
    "lon":12.617040,
    "appid":api_key,
}
response = requests.get(OWM_endpoint, params=weather_params)
print(response.status_code)


