height = float (input("insert the height\n"))
weight = int (input ("insert your weight\n"))
if height > 2.5:
    raise ValueError ("l'altezza umana non dovrebbe superare i 2.5 metri")
#quanto sopra mi dice quando potrebbe essere utile un raise mio, in fase di check 

bmi = weight /(height**2)
print (bmi)