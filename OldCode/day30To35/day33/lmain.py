print ("hello")
import requests
risposta = requests.get(url = "http://api.open-notify.org/iss-now.json")
#NOW RISPOSTA has data in json
data = risposta.json() #now you have the data 
print (data)
position_dict = data["iss_position"]
print (position_dict)
#convert longitude and latitude in a tuple
longitude = position_dict["longitude"]
latitude = position_dict["latitude"]
position = (longitude, latitude)
print (position)

