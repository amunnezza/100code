import random
import turtle as turtle_module
turtle_module.colormode(255)
color_list = []
for i in range (30):
    color_list.append((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
tim = turtle_module.Turtle()
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)



screen = turtle_module.Screen()
screen.exitonclick()