nome1 = input("inserisci il primo nome ")
nome2 = input ("inserisci il secondo nome ")

nome1_lower = nome1.lower()
nome2_lower = nome2.lower()
somma_nomi = nome1_lower +  nome2_lower
decine = 0

for lettera in "true":
    decine += somma_nomi.count(lettera)

unita = 0
for lettera in "love":
    unita += somma_nomi.count(lettera)
totale = decine * 10 + unita
print (f"your score is {totale}")

