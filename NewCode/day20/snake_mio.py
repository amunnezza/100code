STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0) ]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:  #PUNTO 1 per tradizione la classe maiuscola
    def __init__(self) -> None:
        self.segments = []
        self.create_snake() #PUNTO 2 il primo metodo della classe sara quindi create_snake
        self.head = self.segments[0]
    
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
        for seg_number in range (len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number-1].xcor()
            new_y = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.segments[0].heading() == DOWN:  #QU3ESTI PER NON TORNARE SUI PROPRI PASSI
            pass
        else:
            self.segments[0].setheading(UP)  
    
    def down(self):
        if self.segments[0].heading() == UP:
            pass
        else:
            self.segments[0].setheading(DOWN)  

    def left(self):
        if self.segments[0].heading() == RIGHT:
            pass
        else:
            self.segments[0].setheading(LEFT)  
    
    def right (self):
        if self.segments[0].heading() == LEFT:
            pass
        else:
            self.segments[0].setheading(RIGHT)  




        