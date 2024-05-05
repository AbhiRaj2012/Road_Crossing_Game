from turtle import Turtle

ALIGNMENT = "center"
FONT = ("comic_sans", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")

        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-250, 265)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_level()

    def restart(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
