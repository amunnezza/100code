class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe (self):
        print ("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print ("moving in water")
    
    def breathe(self): #overload ??? aggiunta funzionalita
        super().breathe()   #ha quello che ha la superclass
        print ("doing it underwater")   # e quisto lo sovraccarichi
nemo = Fish()

nemo.swim()
nemo.breathe()
print (nemo.num_eyes)
#torna a cherrytree