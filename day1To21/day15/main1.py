#MENU MODELLA I TRE TIPI DI BEVANDA CON COSTO, INGREDIENTI
MENU = {

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
#QUI MODELLA LE RISORSE CHE LA MACCHINA PUO CONTENERE
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


is_on = True


# TODO: 1. Print a Report of caffe machine reource
while is_on:
    choice = input ("Cosa vuoi? espresso / latte / cappuccino")
    if choice == "off":
        is_on = False #ed esci
    elif choice == "report":
        print ("water: 300")
        print ("milk: 200")
        print ("coffee:100")
        print ("money : $ 0")

# TODO : 2 Check if resource are sufficient

# TODO PROCESS COIN 

# TODO CHECK TRANSACTION SUCCESSFULL 

# TODO MAKE COFFEE (UPDATING RESOURCES)

# FIXME 
