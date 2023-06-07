from tkinter import *
from tkinter import messagebox
import random
import os
import pyperclip
working_dir = os.path.realpath(os.path.dirname(__file__))
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password) #LA COPIA IN APPUNTI
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)== 0 or len(password)== 0:
        messagebox.showinfo(title="OOPS ", message="Vedi che hai lasciato un campo vuoto")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Questi sono i dettagli\n"
                                    f"Website: {website} \nEmail: {email}\nPassword: {password}\nTi va bene?")
        if is_ok:
            with open(working_dir + "/data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password} \n")
                website_entry.delete(0, END)
            #email_entry.delete(0, END)
                password_entry.delete(0, END) 



    
# ---------------------------- UI SETUP ------------------------------- #
#INIZIA CON IMMAGINE 200 PER 200 IN UN CANVAS CON 20 DI PADDING SU TUTTI I LATI E LA WINDOW 
#DEVE AVERE IL TITOLO PASSWORD MANAGER
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file= working_dir + "/logo.png")
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
email_entry.insert(0, "luciociotola@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text= "Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text= "Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()