STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0) ]
from turtle import Turtle
class Snake:  #PUNTO 1 per tradizione la classe maiuscola
    def __init__(self) -> None:
        self.segments = []
        self.create_snake() #PUNTO 2 il primo metodo della classe sara quindi create_snake
    
    def create_snake(self):    #simile a quanto  gia visto
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color ("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)   #nota che devi mettre self.segments
    #fine punto 2

    #PUNT 3 adesso devi vedere il metodo move per seguire la testa di snake ed ho

    def move (self):
        


        