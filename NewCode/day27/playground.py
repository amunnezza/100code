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

def stampa_primo_terzo (*args):
    print (args    [0])
    print (args[2])

stampa_primo_terzo(1,2,4,16)

 #inizio video 249

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
# macchina2 = Car()        #questo da errore perchè non trova gli argomenti made e model previsti
# print (macchina2.model)
# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")  #non da errori usando get() e crea oggetto
print(my_car.model)

