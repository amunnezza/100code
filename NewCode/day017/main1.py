#supponi di avere sito web e ti serve un oggetto user

# class User:
#     pass
#     #questo non fa niente

# utente_1 = User()
# #pero funziona
# print (utente_1)
#2 osserva che pratica comune scrivere nome delle classi con PascalCase
# per es class NomeDellaClasse:
         #   eccetera
# 3 diverso da camelCase perchè in camel il primo minuscole e le altre maiuscole poco usato in pyhton
# esitste anche snake_case usato per tutto tranne nome classi     
# 4 nota che potrei ora aggiungere attributi all'oggetto creato 
# per esempio leggittimo fare
# utente_1.id = "001"
# utente_1.username = "luciano"
# print (utente_1.id)     
#ma se per ogni object devi creare sempre le stesse attribute?
#5 entra in gioco constructor per starting point 
#initialize 
#constructor is a special function and python know this because this method 
#have double underscore
#to beginning and end. Is something like this
class Car:
    def __init__(self, seats):
        #here you can initialize attribute
        # pass
        self.seats = seats

my_car = Car(5) # 5 is the variable seats of the object 
#6 **importante** init called every time i create an object
#7 applichiamo a user
# class User :
#     def __init__(self, user_id, username) :
#         self.id = user_id
#         self.username = username
#         self.follower = 0
#     pass


#print (utente_1.username + " " + utente_1.id )
#osserva con constructor devi poi fornire i parametri richiesti quando crei oggetto
# posso anche fissare dei valori di default per gli attributi come ad esempio follower sopra 
#e funziona come vedi 
#print (f"attualmente il numero di follower è {utente_1.follower}")

#10 vai a cherrytree 

#torna da cherryTree

class User :
    def __init__(self, user_id, username) :
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    def follow (self, user):   #nota che self ci va sempre cosi il metodo sa che deve laroare sulloggetto
        """vuole come parametro un utente della Classe User da seguire""" 
        user.follower +=1
        self.following += 1 #incrementa di uno i follower di quello che segui e aumenti il tuo numero
                            #di quelli che stai seguendo
utente_1 = User("001", "luciano")
utente_2 = User ("002", "francesca")
utente_1.follow(utente_2)    
print (utente_1.follower)
print ("dovrebbe essere 0")
print (utente_1.following)
print ("dovrebbe essere 1")
print (utente_2.follower)
print ("dovrebbe essere 1")
print (utente_2.following)
print ("dovrebbe essere 0")
        
