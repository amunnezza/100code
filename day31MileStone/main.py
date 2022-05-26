from tkinter import * #1
BACKGROUND_COLOR = "#B1DDC6"

window = Tk() #2
window.title("Flashy")  #3
window.config (padx=50, pady=50, bg=BACKGROUND_COLOR) #4

canvas = Canvas(width=800, height=526) #5 create the canvas same size of backgroun image
card_front_img = PhotoImage("./day31MileStone/images/card_front.png") #6 prepari immagine
canvas.create_image(400, 263, image=card_front_img) #7 posizioni al centro
canvas.grid(row=0, column=0) #8 in griglia prima riga e colonna 
canvas.config (bg=BACKGROUND_COLOR, highlighthickness=0) #9 per avere tutto verde

 



window.mainloop()


