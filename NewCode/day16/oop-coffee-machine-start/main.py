from menu import Menu, MenuItem   #iniziato importando le classi che mi intressano per risolvere
                                  #l'esercizio
from coffee_maker import CoffeeMaker    #sono documentate 
from money_machine import MoneyMachine

#1 print report

money_machine = MoneyMachine()

money_machine.report() #fatto il primo 

coffee_maker = CoffeeMaker()
coffee_maker.report()
# 2 fino a ora ha fatto tutto lui

#check resource sufficient
is_on = True
#3 crea un oggetto menu e poi va in azione 
menu = Menu()
while is_on:
    options = menu.get_items()
    choice = input (f"What would you like? {options}")
    if choice  == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else: #da qui inizia l'azione
        drink = menu.find_drink(choice)
        #print (drink)
        #4 check if resource sufficiente
        if (coffee_maker.is_resource_sufficient(drink)):
            if (money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink) 

##osservazione finale 
#facilitato la lettura del codice e senza spaghetti da tutte le parti

#torna a cherryTree


