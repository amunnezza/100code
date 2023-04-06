import math
conto = float(input ("What was the total bill? $"))
#conto_float = float (conto)
mancia = int (input ("How much tip would you like to give? 10, 12, or 15?"))
#mancia_int = int(mancia)
n_persone = int (input("How many people to split the bill?"))
totale = conto + mancia * conto /100
print (totale)
costo_persona = totale / n_persone
costo_persona_2cifre = math.ceil(costo_persona*100)/100
print (f"Each person should pay: ${costo_persona_2cifre}")
