"""
1   objective : send a motivational quote via email on the current day of week
    - use datetime to check current day of week
    - openn motivational text file for a list of quotes
    - use random to take a random quotes
    - finally use smtplib to send the email 
    
"""
import datetime as dt
from multiprocessing import connection
import smtplib
import random
import os

MY_EMAIL = "l.ciotola58@gmail.com"
MY_PASSWORD = "uirsncxbgpdcffus" #"Iaggymle12i!"

working_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(working_dir)

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
week_day = now.weekday()
if week_day == 6:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        print (type(all_quotes))
        with open ("./copia.txt", "w") as copia:
            for item in all_quotes:
                copia.write(item)
        quote = random.choice(all_quotes)
    print (quote)
    with  smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail (from_addr=MY_EMAIL, 
                            to_addrs="luciociotola@gmail.com",
                            msg = f"Subject:il giorno giusto\n\n{quote}")
    
   
    


# #posso anche creare un datetime
# date_of_birth = dt.datetime (year=1965, month=1, day=13) #le ore di default sono a 0
# print (date_of_birth)
# print (date_of_birth.weekday()) #curiosita mia 




# my_email = "l.ciotola58@gmail.com"
# my_passwrd = "Iaggymle12i!"


# messaggio = "prova di funzionamento 2"

# connection.sendmail(from_addr=my_email, to_addrs="luciociotola@gmail.com", msg=f"Subject:Hello\n\n{messaggio}")
# connection.close()

