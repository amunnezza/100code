# question_data = [

#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
#TODO DO NOT CHANGE NAME OF VARIABLE- MAKE A get request getting 10 question and result
#parsed get into question_data
#hint: create a dictionary for amount and type parameter

import requests

parameters = {
    "amount":10, 
    "type":"boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print (question_data)