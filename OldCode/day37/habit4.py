""" A questo punto cerchiamo di creare un sistema di automatismo che 
riguardi la data in maniera da non doverla creare io ogni volta ma che 
si cambia automaticamente quando laqncio lo script
"""
from datetime import datetime
import requests
USERNAME = "luciociotola"
TOKEN = "Nmdcdnvmriusosclrves2022"

pixela_endpoint = "https://pixe.la/v1/users"


GRAPHID = "graph1"

user_params ={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}

graph_config = {
    "id":"graph1",
    "name":"minuti di programmazione",
    "unit":"minuti",
    "type": "float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

today = datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {
    "date": strformat"20220616",
    "quantity":"120",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print (response)