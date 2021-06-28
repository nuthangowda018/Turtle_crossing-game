from turtle import  Screen
import time
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard

screen=Screen()
screen.screensize(600,600)
screen.title("CROSSING_GAME")
screen.tracer(0)

player=Player()
car_manager=Car_manager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(key="Up",fun=player.go_up)



is_on=True
while is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.mov_car()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            is_on=False
            scoreboard.game_over()

    if player.ycor()>280:
        player.goto(0,-280)
        car_manager.level_up()
        scoreboard.update_score()









screen.exitonclick()