import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Us State game")
image = "./day25/finale/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# """ def get_mouse_click_coor(x, y):
#     print (x, y)
#  """
#turtle.onscreenclick(get_mouse_click_coor)
#per trovare le coordfinate ma gia presenti in csv
answer_state = screen.textinput(title ="Guess the state", prompt ="whats a State?")
print (answer_state)
turtle.mainloop()
#TODO CONVERT GUESS TO TITLE CASE
data = pd.read_csv ("./day25/finale/50_states.csv")
print (data) 
all_states = data.state.to_list()

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    print (answer_state)
    t.goto( int(state_data.x), int(state_data.y))
    t.write(answer_state)

#TODO CHECK IF THE GUESS IS AMONG 50 SSTATES
    #
#TODO WRITE CORRECT GUESSES ON MAP
    #
    #USE A LOOP TO ALLOW THE USER TO KEEP GUESSING
#RECORD CORRECT GUESSES IN A LIST
#KEEP TRACK OF THE SCORES






#screen.exitonclick()


