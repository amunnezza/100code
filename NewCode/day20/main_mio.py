from turtle import Turtle, Screen
import time
from snake_mio import Snake

screen = Screen()
screen.setup( width= 600, height = 600)
screen.bgcolor("black") 
screen.title("My snake game")
screen.tracer(0) # annulla aggiornamento continuo

snake = Snake()
#qui per il movimento
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep (0.1)
    snake.move()
    
screen.exitonclick()