from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup( width= 600, height = 600)
screen.bgcolor("black") 
screen.title("My snake game")
screen.tracer(0) # annulla aggiornamento continuo

#1 create a snake body
#every turtle is 20 x 20 and get 3 squre adjacent
starting_position =[(0,0), (-20,0), (-40,0)]
segments = []
for position in starting_position :
    new_segment = Turtle("square")
    new_segment.color ("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update() #per dare senso di movimento
    # for seq in segments:
    #     seq.forward(20)
    time.sleep(0.1)
    #il codice che segue basa tutto sul fatto che parti dall'ultimo e gli fai 
    #assumere la posizione del precedente e cosi via su tutta la catena con il
    #primo che è l'ultimo a muoversi e detta lui la direzione del movimento!!!
    for seg_num in range (len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)  
    segments[0].forward(20)
    segments[0].left(90)


#per girare fai assumere all'ultimo la posizione del precedente e cosi via 
#cambi il modo di muoversi e se gira gli altri losegueno

#equivale al seguente codice 
# segment_1 = Turtle("square")
# segment_1.color ("white")

# segment_2 = Turtle("square")
# segment_2.color ("white")
# segment_2.goto (-20, 0)

# segment_3 = Turtle("square")
# segment_3.color ("white")
# segment_3.goto(-40, 0)

#FASE 184 ANIMATE THE SNAKE IJNITIALLY MOVE AUTOMATIC


screen.exitonclick()
