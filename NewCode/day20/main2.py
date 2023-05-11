from turtle import Screen, Turtle
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")



starting_positions = [(0,0),  (-20,0), (-40,0)]

segmenti = []

for coord in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(coord)
    segmenti.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_number in range (len(segmenti)-1, 0, -1):
        new_x = segmenti[seg_number-1].xcor()
        new_y = segmenti[seg_number-1].ycor()
        segmenti[seg_number].goto(new_x, new_y)
    segmenti[0].forward(20)
    if segmenti[0].xcor() > 290:
        game_is_on = False

screen.exitonclick()
