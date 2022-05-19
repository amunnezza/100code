from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image= logo_img)
# esclusoo perchè usi grid canvas.pack() quindi devi mettere canvas in the grid
canvas.grid(row=0, column=1)
#crea le label e posizioni in grid
website_label = Label(text="Website:")
website_label.grid (row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
#poi vengono le entries con larghezza e posizione in grid opportune
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text= "Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text= "Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()