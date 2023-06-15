#scopo è far girare le carte
from tkinter import *   
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import os

working_dir = os.path.realpath(os.path.dirname(__file__))#imposta directory funzionamento

#1 apri il file csv e ogni riga parola e traduzione
data = pandas.read_csv(working_dir + "/data/french_words.csv")
to_learn = data.to_dict(orient="records")
print (to_learn)
#poi crea quello che serve 
def next_card():
    pass  


window = Tk() 
window.title("Flashy")  
window.config (padx=50, pady=50, bg=BACKGROUND_COLOR) #4

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(working_dir + "/images/card_front.png") 
canvas.create_image(400, 263, image=card_front_img) #
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))#
canvas.config (bg=BACKGROUND_COLOR, highlightthickness=0) # 
canvas.grid(row=0, column=0, columnspan=2) #

cross_image = PhotoImage(file=working_dir+"/images/wrong.png") #
unknown_button = Button(image=cross_image, command=next_card)  #
unknown_button.grid(row=1, column=0)#

check_image = PhotoImage(file=working_dir+ "/images/right.png") #
known_button = Button(image=check_image, command=next_card) #ai button dai un comando da eseguire
known_button.grid(row=1, column=1)  

window.mainloop()





