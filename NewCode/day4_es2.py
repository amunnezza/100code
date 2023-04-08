# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#hai gia la lista devi prendere un indice a caso
import random
indice_caso = random.randint(0, len(names)-1) 
print (indice_caso)
print (f"chi paga deve essere {names[indice_caso]}") 
print ("funziona anche con random.choice(names)")
nome_che_paga = random.choice(names)
print(f"chi paga deve essere {nome_che_paga}")

#Write your code below this line 👇
