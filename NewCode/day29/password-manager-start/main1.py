from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady=20)
#working_dir = __file__
working_dir = os.path.realpath(os.path.dirname(__file__))
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file= working_dir + "\logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.pack()

window.mainloop()