import requests

pixela_endpoint = "https://pixe.la/v1/users"

#creiamo un utente
""" curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes",
 "notMinor":"yes"}'
{"message":"Success.","isSuccess":true}

quanto sopra diventa usando la libreria requestos con il metodo post
"""

user_params ={
    "token": "Nmdcdnvmriusosclrves2022",
    "username":"luciociotola",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

