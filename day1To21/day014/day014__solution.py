from art import logo, vs
from game_data import data
import random
# A)Display art
print (logo)
# B)Ci sono due personaggi random da prendere da un dizionario a parte
def format_data (account):
    """Format account pronto alla stampa"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """use if statement to check if answer is right"""
    if a_follower > b_follower:
        if guess == "a":
            return True
    else:
        return guess == "b"   #invece di tutto il pastrocchioi sopra



account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b: #molto improbabile ma puo accadere
    account_a = random.choice(data)


# c) vedere come strutturarli per la stampa


print (f"Compare A {format_data(account_a)}")
print (vs)
print (f"Against B {format_data(account_b)}")

# d) ask user for a guess
guess = input ("who has more followers, type 'A' or 'B'").lower() #cosi input consistente

# e) check if user is correct
#     --- Get follower 
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

#     -- check if user is correnct
# usando una funzione a parte sopra check_answer()
is_correct = check_answer (guess, a_follower_count, b_follower_count)
# f) give user feedback on their guess
if is_correct:
    score += 1  #traccia il risultato
    print (f"You are right, your score is {score}")
else: 
    print (f"you are wrong. Your final score is {score}")

# g) Score keeping

# h) make games repeatable creando una 

# i)making the account in position B become the next account 
# in position A

# l) clear the screen between rounds


# poi vai all'editor 