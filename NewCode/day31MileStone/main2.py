#scopo è far girare le carte 
from tkinter import *   
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
import os
working_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(working_dir) #ladirectory di lavoro ora è dove si trova il file


#1 apri il file csv e ogni riga parola e traduzione
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records") #1-bis  osserva opzione orient per salvare in dict in formato che interessa
#di base una lista di dizionari e ogni dizionario ha due chiavi French e English con dati la stessa parola 
#in french and english appunto
#print (to_learn)
current_card = {}
#poi crea quello che serve 
def next_card():
    #2 una volta creata la lista di dizionari al punto 1 ne prendi uno random e lo metti in punto 3
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn) 
    #print (current_card["French"])
    canvas.itemconfig(card_title, text = "French", fill="black") #3 metti il titolo french
    canvas.itemconfig(card_word, text= current_card["French"], fill="black") #e sotto una parola random 
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  #fa girare la carta dopo 3000 ms per ogni carta

def flip_card():
    canvas.itemconfig (card_title, text="English", fill="white")
    canvas.itemconfig( card_word, text = current_card["English"], fill = "white" )
    canvas.itemconfig(card_background, image=card_back_img ) 



window = Tk() 
window.title("Flashy")  
window.config (padx=50, pady=50, bg=BACKGROUND_COLOR) #4

flip_timer = window.after(3000, func=flip_card)  #fa girare la carta dopo 3000 ms

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png") 
card_back_img = PhotoImage(file="./images/card_back.png") 
card_background = canvas.create_image(400, 263, image=card_front_img) #

#3 crea variabili in cui mettere il frutto di next card 
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))#
canvas.config (bg=BACKGROUND_COLOR, highlightthickness=0) # 
canvas.grid(row=0, column=0, columnspan=2) #

cross_image = PhotoImage(file="./images/wrong.png") #
unknown_button = Button(image=cross_image, command=next_card)  #
unknown_button.grid(row=1, column=0)#

check_image = PhotoImage(file="./images/right.png") #
known_button = Button(image=check_image, command=next_card) #ai button dai un comando da eseguire
known_button.grid(row=1, column=1)  


next_card() #metti subito French e una parola 
window.mainloop()





