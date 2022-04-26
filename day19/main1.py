from turtle import Turtle, Screen
from xmlrpc.server import SimpleXMLRPCRequestHandler

tim = Turtle()
screen = Screen()
def move_forwards():
    tim.forward(10)

screen.listen()  #in ascolto
screen.onkey(key = "space", fun = move_forwards) #cosa fa quando premi space 


screen.exitonclick()






