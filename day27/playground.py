from tkinter import N


def add (*args):
    somma = 0
    for number in args:
        somma += number
    return somma


print (add(1, 2, 3, 4))


def calculate (n,**kwargs):
    print (kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


    
print (calculate (2,add = 3, multiply = 5))
