from turtle import Screen, Turtle
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")



starting_position = [(0,0),  (-20,0), (-40,0)]

segmenti = []

for coord in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(coord)
    
    
    segmenti.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segmenti:
        seg.forward(20)
        if seg.xcor() > 300:
            game_is_on = False


screen.exitonclick()