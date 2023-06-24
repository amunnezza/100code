""" Verifica se la data è in qualcuna delle date in file csv 
se è cosi scrivi una mail prendendo uno dei template a caso 
"""

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv 

# 2. Check if today matches a birthday in the birthdays.csv

from datetime import datetime  
import pandas
import random
import smtplib
MY_EMAIL = "l.ciotola58@gmail.com"
MY_PASSWORD = "Iaggymle12i!"

today_tuple = (datetime.now().month,datetime.now().day) 
print (today_tuple)

data = pandas.read_csv("./day32/birthdaywisherstart/birthdays.csv")
#print (data)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#templates cohomprehension 
#new_dict = ={new_key:new_value for (index, data_row) in data.iterrows()}

birthdays_dict =  {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}
print (birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./day32/birthdaywisherstart/letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print (contents)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        print (birthday_person["email"])
        connection.sendmail (from_addr=MY_EMAIL, 
                            to_addrs= birthday_person["email"],
                            msg = f"Subject:Happy birthday!\n\n{contents}")
    

# 4. Send the letter generated in step 3 to that person's email address.




