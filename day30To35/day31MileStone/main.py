from audioop import cross
from msilib import knownbits
from tkinter import * #1
BACKGROUND_COLOR = "#B1DDC6"

window = Tk() #2
window.title("Flashy")  #3
window.config (padx=50, pady=50, bg=BACKGROUND_COLOR) #4

canvas = Canvas(width=800, height=526) #5 create the canvas same size of backgroun image
card_front_img = PhotoImage("./day31MileStone/images/card_front.png") #6 prepari immagine
canvas.create_image(400, 263, image=card_front_img) #7 posizioni al centro
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))#10 il testo da tradurre
canvas.config (bg=BACKGROUND_COLOR, highlightthickness=0) #9 per avere tutto verde
canvas.grid(row=0, column=0, columnspan=2) #8 in griglia prima riga e colonna e 15 columnspand per posizione

cross_image = PhotoImage(file="./day31MileStone/images/wrong.png") #11 crea image da mettere nel button
unknown_button = Button(image=cross_image)  #12 fa  il button
unknown_button.grid(row=1, column=0)#posiziona

check_image = PhotoImage(file="./day31MileStone/images/right.png") #13 stesso discorso per il medesimo button
known_button = Button(image=check_image)
known_button.grid(row=1, column=1)  

window.mainloop()

#FINE MAIN CONTINUA IN MAIN1.PY
