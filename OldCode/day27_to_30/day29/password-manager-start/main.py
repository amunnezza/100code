from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.pack()

window.mainloop()