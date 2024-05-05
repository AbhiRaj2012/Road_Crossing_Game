import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.bgcolor("gray80")
screen.title("The Road Crossing Game")
screen.setup(600, 600)
screen.tracer(0)
track = Road()
score = Scoreboard()
turtle_player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle_player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            score.restart()

    if turtle_player.ycor() > 250:
        turtle_player.level_up()
        score.increment_level()
        car_manager.speed_up()

    screen.update()

screen.exitonclick()
