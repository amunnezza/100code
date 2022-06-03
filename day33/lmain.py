print ("hello")
import requests
risposta = requests.get(url = "http://api.open-notify.org/iss-now.json")
print (risposta)
risposta_errata = requests.get(url= "http://www.lkjhsadfp9adshf.com")
print (risposta_errata)
risposta_errata.raise_for_status()