from turtle import Turtle


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey40")
        self.hideturtle()
        self.penup()
        self.pensize(10)
        self.goto(-300,-245)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()
        self.goto(300,245)
        self.pendown()
        self.setheading(180)
        self.forward(600)

