import smtplib

my_email = "l.ciotola58@gmail.com"
my_passwrd = "uirsncxbgpdcffus"   #password Iaggymle12i! qui usi password per app

connection= smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_passwrd)
messaggio = "prova di funzionamento nuova"

connection.sendmail(from_addr=my_email, to_addrs="luciociotola@gmail.com", msg=f"Subject:Hello\n\n{messaggio}")
connection.close()

