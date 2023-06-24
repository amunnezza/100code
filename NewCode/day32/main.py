import smtplib

my_email = "l.ciotola58@gmail.com"
my_passwrd = "Iaggymle12i!"

connection= smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_passwrd)
messaggio = "prova di funzionamento 2"

connection.sendmail(from_addr=my_email, to_addrs="luciociotola@gmail.com", msg=f"Subject:Hello\n\n{messaggio}")
connection.close()

