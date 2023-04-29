#Number Guessing Game Objectives:

# Include an ASCII art logo.
##from site http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

print ("""

  ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ !
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/       

""")
print ("benvenuto al classico gioco indovina il numero")

EASY_LEVEL_TURNS = 10
HIGH_LEVEL_TURNS = 5

# Include two different difficulty levels (e.g., 10 gueses in easy mode, 
# only 5 guesses in hard mode).
def set_difficulty():
    level = input("Set difficolta 'easy' or 'high': ")
    if level == "easy":
        return   EASY_LEVEL_TURNS
    elif level == "high":
        return HIGH_LEVEL_TURNS
   
turns = set_difficulty()
print (f"Hai ancora {turns} tentativi rimasti")
# Allow the player to submit a guess for a number between 1 and 100.
guess = int (input("Indovina il numero giusto fra 1 e 100 "))


# Check user's guess against actual answer. Print "Too high." or "Too low." 
# depending on the user's answer.
def check_answer (answer, guess):
    if answer > guess :
        print ("Too low")
    elif guess > answer :
        print ("Too high")
    else:
        print (f"You got it. The answer is {answer}")


# Chiaramente  devi prima assegnare la risposta giusta con un random (importa libreria)
#e per debug conviene stampare il numero scelto
import random
answer = random.randint(1, 100)
print (f"Psst la risposta giusta is {answer}")
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
