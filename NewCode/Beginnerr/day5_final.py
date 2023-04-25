#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_len = len(letters)
numbers_len = len(numbers)
symbols_len = len(symbols)
password = ""
for indice in range(nr_letters):
    password += letters[random.randint(0, letters_len -1)]

for indice in range(nr_symbols):
    password += symbols[random.randint(0, symbols_len -1)]

for indice in range(nr_numbers):
    password += numbers[random.randint(0, numbers_len - 1)]


print (password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password1 = ""
rand_choice = random.randint(0,2)

list_rimanenze = [nr_letters, nr_symbols, nr_numbers]
len_password = nr_letters + nr_symbols + nr_numbers
while len_password != 0:
    rand_choice = random.randint(0,2)
    if rand_choice == 0 and list_rimanenze [0] != 0:
        password1 += letters[random.randint(0, letters_len -1)]
        len_password += -1
        list_rimanenze[0] = list_rimanenze[0] -1 
    elif rand_choice == 1 and list_rimanenze [1] != 0:
        password1 += symbols[random.randint(0, symbols_len -1)]
        len_password += -1
        list_rimanenze[1] = list_rimanenze[1] -1  
    elif rand_choice == 2 and list_rimanenze [2] != 0:
        password1 += numbers[random.randint(0, numbers_len -1)]
        len_password += -1
        list_rimanenze[2] = list_rimanenze[2] -1  
    else:
        continue
        

print (password1)
        
