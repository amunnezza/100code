import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey (player.go_up ,"Up")  #METODO SENZA PARENTESI

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with a cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False #stop the game
            scoreboard.game_over()
    #detect other part of the screen success
    #usa un metodo in player
    if player.is_at_finish():
        #torna all inizio con altro metro di player
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()