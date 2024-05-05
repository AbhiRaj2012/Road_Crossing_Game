from turtle import Turtle
import random

COLORS = ["red", "blue", "gold1", "SeaGreen1", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
TRACKS = [-230, -210, -190, -170, -150, -130, -110, -90, -70, -50, -30, -10,
          10, 30, 50, 70, 90, 110, 130, 150, 170]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = (-230 + 23 * random.randint(0, 20))
            new_car.goto(340, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
