#import turtle  # 1 importa da libreria di default
from turtle import Turtle, Screen # 7 importa la blueprint per la creazione di un oggetto Turtle e di oggetti Screen 
import anothe_module # 2importa dal file another_module.py scritto nella stessa dir

#print (anothe_module.another_variable)   #3 osserva il modo di chiamare usando nomeModulo.noveAttributo

timmy = Turtle() #5 chiama costruttore e crea oggetto di tipo Turtle con nome timmy  
                        # 6 potevo semplifica facendo from turtle import Turtle 
                                                      #timmy = Turtle()  
## torna a cherryTree
print (timmy ) # ci dira che è un oggetto )
my_screen = Screen()
print (my_screen.canvheight) # 7 stampa altezza dello screen che è un attributo vai ora a cherrytree per parlare di metodi
timmy.shape("turtle")  #9 altro uso di metodo per cambiare forma all'oggetto timmy
timmy.color("red", "coral") #oppure cambiare colore 
my_screen.exitonclick() #9 dimostra uso di uno dei metodi e mostra lo screen fino a che non ci cliccki sopra
#nota bene la documentazione è presente
timmy.forward(100) #10 si muove di 100 passi 
#11 torna a cherrytree per vedere come usare altre librerie 


