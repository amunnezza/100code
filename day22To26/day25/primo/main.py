# with open ("./day25/weather_data.csv") as data_file:
    
#     data = data_file.readlines()
#     print (data)

# import csv 

# with open ("./day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print (data) #crea un oggetto csv
#     temperatures = []
#     for row in data:
#         print(row) # crea un vettore di liste ogni lista una riga 
#                     #in pratica ogni riga diventa una lista
#         #l'utilita è per esempio vuoi avere tutte le temperature in formato integer in una
#         #nuova lista chiamata temperatures = []
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         else: 
#             pass

#     print (temperatures)

#usasndo panda è piu semplice

import pandas

data = pandas.read_csv("./day25/primo/weather_data.csv")
# print (data)
# structures = data["temp"]
# print (structures)
# #per ottenere una media delle temperature 
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print (average_temp)
# #ma anche con 
# altro_average = data["temp"].mean()
# print (altro_average)
# #nb esistono molti altri method come 
# print (data["temp"].max())


#per filtrare ad esempio se voglio day is monday usa
#print (data)

nuovo = data[data.day == "Monday"] #tra parentesi il filtro
print (nuovo)
#ma posso ancora filtrare  se per esempio di quel giorno voglio le condition
print (nuovo["condition"])

#which row have the max temperature

max_temp_row = data [data.temp == data.temp.max()]
print (max_temp_row)

# se voglio converitre in Fhareneti con la formula celsius x 9/5 + 32
monday_temp = int (nuovo.temp)
print (monday_temp*5/9 + 32)

# to create a data frame from scratch?
#parti da 
data_dict ={
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_frame = pandas.DataFrame(data_dict)
print (new_frame)

#converti in csv
new_frame.to_csv ("./day25/primo/altro.csv") 