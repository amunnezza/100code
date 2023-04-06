from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()  #in ascolto
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backwards(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
screen.onkey(key = "w", fun = move_forwards)   
screen.onkey(key = "s", fun = move_backwards)  
screen.onkey(key = "a", fun = turn_left)  
screen.onkey(key = "d", fun = turn_right) 

screen.exitonclick()