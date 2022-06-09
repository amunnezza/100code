""" uso datetime module"""
import datetime as dt
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

