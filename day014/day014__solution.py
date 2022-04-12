from art import logo
from game_data import data
import random
# A)Display art
print (logo)
# B)Ci sono due personaggi random da prendere da un dizionario a parte
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b: #molto improbabile ma puo accadere
    account_a = random.choice(data)


# c) vedere come strutturarli per la stampa
def format_data (account):
    """Format account pronto alla stampa"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

print (f"Compare A {format_data(account_a)}")
print (f"Compare B {format_data(account_b)}")

# d) ask user for a guess

# e) check if user is correct
#     --- Get follower 
#     -- check if user is correnct
# f) give user feedback on their guess

# g) Score keeping

# h) make games repeatable

# i)making the account in position B become the next account 
# in position A

# l) clear the screen between rounds


# poi vai all'editor 