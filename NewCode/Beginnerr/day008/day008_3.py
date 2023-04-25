
'''Scopo è calcolare numero di lattine di vernice necessarie
per dipingere una parete data altezza e larghezza
NB il numero di lattine è l'INTERO superiore'''

from math import ceil

#3
def paint_calc(height, width, cover):
    area = height * width
    num_can = area / cover
    return ceil(num_can)

print  ("CALCOLO NUMERO LATTINE")
cover = int (input("una lattina quanti metri copre?"))
height = float (input("quale è l'altezza?"))
width = float (input("Quale è larghezza?"))

num_latt = paint_calc(height, width, cover)
print (f"Il numero di lattine è {num_latt}")