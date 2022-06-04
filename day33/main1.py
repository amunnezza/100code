import requests
MY_LAT = 42.051780
MY_LONG = 12.617040

parameters ={
    "lat":MY_LAT,
    "long":MY_LONG,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print (data)
