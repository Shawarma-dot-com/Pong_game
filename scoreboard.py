from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-200, 200)
        self.write(f"score: {self.l_score}", align="center", font=("Courier", 15, "normal"))
        self.goto(200, 200)
        self.write(f"score: {self.r_score}", align="center", font=("Courier", 15, "normal"))

    def l_update(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_update(self):
        self.clear()
        self.r_score += 1
        self.update_score()