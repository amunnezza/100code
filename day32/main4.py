"""
1   objective : send a motivational quote via email on the current day of week
    - use datetime to check current day of week
    - openn motivational text file for a list of quotes
    - use random to take a random quotes
    - finally use smtplib to send the email 
    
"""
import datetime as dt
import smtplib

my_email = "l.ciotola58@gmail.com"
my_passwrd = "Iaggymle12i!"


#vediamo se prendo ora 
now = dt.datetime.now()

print (now)
#stringa complessa ma posso prendere parti come anno, mese, gg. e giorno della settimana
print (now.year)
print (now.month)
print (now.day)
print (now.weekday())

#posso anche creare un datetime
date_of_birth = dt.datetime (year=1965, month=1, day=13) #le ore di default sono a 0
print (date_of_birth)
print (date_of_birth.weekday()) #curiosita mia 




my_email = "l.ciotola58@gmail.com"
my_passwrd = "Iaggymle12i!"

connection= smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_passwrd)
messaggio = "prova di funzionamento 2"

connection.sendmail(from_addr=my_email, to_addrs="luciociotola@gmail.com", msg=f"Subject:Hello\n\n{messaggio}")
connection.close()

