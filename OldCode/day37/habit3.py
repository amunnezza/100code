import requests
USERNAME = "luciociotola"
TOKEN = "Nmdcdnvmriusosclrves2022"

pixela_endpoint = "https://pixe.la/v1/users"

#creiamo un utente
""" curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes",
 "notMinor":"yes"}'
{"message":"Success.","isSuccess":true}

quanto sopra diventa usando la libreria requestos con il metodo post
"""
GRAPHID = "graph1"

"""POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
{"message":"Success.","isSuccess":true}"""
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


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {
    "date":"20220616",
    "quantity":"120",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print (response)