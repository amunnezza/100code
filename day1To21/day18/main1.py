#fare random walk
from turtle import Turtle, Screen, colormode

timmy = Turtle()
screen = Screen()

colormode(255)
import random

colors = []
for i in range (15):
    colors.append((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
directions = [0, 90, 180, 270] #le 4 direzioni
timmy.pensize(25)
timmy.speed ("fastest")

for _ in range (200):
    timmy.color(random.choice(colors))
    timmy.forward(60)
    timmy.setheading(random.choice(directions))
