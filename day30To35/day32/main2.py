"""versione con with ecc. ecc. per evitare di chiudere la connessione"""
import smtplib

my_email = "l.ciotola58@gmail.com"
my_passwrd = "Iaggymle12i!"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_passwrd)
    messaggio = "prova di funzionamento 3 versione con with ecc. ecc. per evitare di chiudere la connessione"
    connection.sendmail(from_addr=my_email, 
                        to_addrs="luciociotola@gmail.com", 
                        msg=f"Subject:Hello\n\n{messaggio}")

