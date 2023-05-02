###This code will not work in repl.it as there is no access 
#to the colorgram package here.###
##We talk about this in the video tutorials##
 #primo esercizio da file 165 dei video disegna un quadrato



from turtle import Turtle, Screen

tim = Turtle()
tim.color ("blue")
tim.shape("classic")
for _ in range (0,4):
    tim.forward(100)
    tim.right(90)


#soluzione per file 167 video
tim.left(90)

for _ in range (0,30):
    tim.color("red")
    tim.forward (2)
    tim.pu()
    tim.forward(10)
    tim.pd()

screen = Screen()
screen.exitonclick()


