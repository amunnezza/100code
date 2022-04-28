from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup( width= 600, height = 600)
screen.bgcolor("black") 
screen.title("My snake game")
screen.tracer(0) # annulla aggiornamento continuo

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update() #per dare senso di movimento
    # for seq in segments:
    #     seq.forward(20)
    time.sleep(0.1)
    #il codice che segue basa tutto sul fatto che parti dall'ultimo e gli fai 
    #assumere la posizione del precedente e cosi via su tutta la catena con il
    #primo che è l'ultimo a muoversi e detta lui la direzione del movimento!!!
    snake.move()
    # how to detect c ollision? usa metodo distance
    if snake.head.distance (food) < 20:  #method distance work if argument is a turtle objiece
        #print ("they collide") # test funzionamento
        #in realta dovrebbe creare un nuovo pallino
        #per farlo crea un nuovo metodo in food che si chiama refresh()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #DETECT COLLIZION WITH WALL

    if snake.head.xcor()  > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False 
        
    #detect collision
    # if head hit any other part of snake game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()     

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
