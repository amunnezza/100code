from turtle import Turtle
import random
## food non è altro che un turtle per cui inherit
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed ("fastest")
        self.refresh() #va chiamata all'inizio
        
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint (-280, 280)
        self.goto(random_x, random_y)


        #giusto per provare