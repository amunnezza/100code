from ast import arg


def funzione (*args):
    print (args)
    for element in args:
        print (element)

funzione ("aspo", 2, 3, "quante ne voglio")


def add (*args):
    somma = 0
    for number in args:
        somma += number
    return somma


print (add(1, 2, 3, 4))

def prova (**kwargs):
    print (kwargs)

prova (add = 3 , multiply = 5)    


def calculate (n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
   
print (calculate (2,add = 3, multiply = 5))

class Car:
    def __init__(self, **kwargs):
        self.made = kwargs["made"]
        self.model = kwargs["model"]
        
macchina = Car(made= "kia", model="stonic")
print (macchina.made)
print (macchina.model)
