# punto 11

from  prettytable import PrettyTable
table = PrettyTable()  #12 creato oggetto gia qui stampa qualcosa
#add columns with relative table

table.add_column ("Pokemon Name ", ["Pikachu", "Squirtie", "Charmander"]) #13 leggi doc per capire come funzionap
table.add_column("Type", ["Electric", "Water", "Fire"])
#13puoi cambiare gli attributi? SI VEDI SOTTO 
table.align = "r"  #ACCEDI E CAMBIA
print (table)