from turtle import Turtle, Screen, colormode

timmy = Turtle()
screen = Screen()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red", "yellow")
# timmy_the_turtle.forward(100)
#screen = Screen()
#screen.exitonclick()
 #read documentation
# read method shape()
#method color())
#check that Turtle is built on Tcl/Tk
#about movement
# forward()
#check on usual site (stackoverflow)
#first challenge is draw square
# for _ in range (4):
#     timmy.forward(100)
#     timmy.left(90)


#punto 167 vuoi disegnare una linea dashed
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#168 crea diverse figure geometriche di diverso colore
colormode(255)
import random

colors = []
for i in range (15):
    colors.append((random.randint(1,255), random.randint(1,255), random.randint(1,255)))

def draw_shapes (num_sides):
    angle = 360 /num_sides
    timmy.color(random.choice(colors))
    for _ in range (num_sides):
        
        timmy.forward(100)
        timmy.right(angle)

for n in range (3,11):
    
    draw_shapes(n)

screen.exitonclick()
#fine 168

#per 169 vai a main1.py

