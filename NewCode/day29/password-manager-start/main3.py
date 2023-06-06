from tkinter import *
from tkinter import messagebox #va messo per importare il modulo
import os
#working_dir = __file__
working_dir = os.path.realpath(os.path.dirname(__file__))
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# come trasporto quello nel programma e salva su file e come cancellare tutto
#quando premi add button. aggiungi save come funzione a button con command
def save ():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title= website, message= f"These are the detail entered \n"
                           f"Email: {email} \nPassword = {password}\nIs it ok to enter?")
    
    if is_ok:
        with open (working_dir + "/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete (0,END)



# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER
#continuando mette le interfacce usando grid e grid span per disporle

window = Tk()
window.title("Password Manager")
window.config(padx = 10, pady=10)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file= working_dir + "/logo.png")
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
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "luciociotola@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

#button
generate_password_button = Button(text = "Generate Password")
generate_password_button.grid (row=3, column=2)

add_button = Button (text= "Add", width=36, command= save)
add_button.grid (row=4, column=1, columnspan=2)

window.mainloop()