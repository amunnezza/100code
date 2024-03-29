from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER
#continuando mette le interfacce usando grid e grid span per disporle

window = Tk()
window.title("Password Manager")
window.config(padx = 10, pady=10)
#working_dir = __file__
working_dir = os.path.realpath(os.path.dirname(__file__))
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file= working_dir + "\logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)
#canvas.pack()
#LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text = "Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#ENTRIES
website_entry = Entry (width=40)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

#button
generate_password_button = Button(text = "Generate Password")
generate_password_button.grid (row=3, column=2)

add_button = Button (text= "Add", width=36)
add_button.grid (row=4, column=1, columnspan=2)

window.mainloop()