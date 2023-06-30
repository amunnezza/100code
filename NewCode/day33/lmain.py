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

<<<<<<< HEAD
=======
#prova con url sbagliata
risposta1 = requests.get(url = "http://api.open-notify.org/nonEsiste.json")
risposta1.raise_for_status()


>>>>>>> 7fa04da70a58889938d65472262eb04083f3e4b4
