import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color ():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range (int (360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading (tim.heading() + size_of_gap)

# qui fai il primo test
#proviamo a cambiare heading
tim.pu()
tim.backward(200)
tim.pd()
draw_spirograph(8)
tim.pu()
tim.forward(400)
tim.pd()
draw_spirograph(8)

screen = t.Screen()

screen.exitonclick()


