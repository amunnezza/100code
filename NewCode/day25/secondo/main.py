"""partendo dal file squirrel creare un piccolo file csv contenente
fur_colour e Count come colonne"""
import pandas as pd

#la partenza è la colonna PrimaryFurColor
data = pd.read_csv("./NewCode/day25/secondo/squirrel.csv" )
print (data["Primary Fur Color"])
gray_squirrels = data [data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len (gray_squirrels)
print (gray_squirrels_count)
cinnamon_squirrels = data [data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len (cinnamon_squirrels)
print (cinnamon_squirrels_count)
black_squirrels = data [data["Primary Fur Color"] == "Black"]
black_squirrels_count = len (black_squirrels)
print (black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"], 
    "Count" : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame (data_dict)
df.to_csv ("./NewCode/day25/secondo/squirrelCount.csv")
