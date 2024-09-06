from turtle import Turtle
UP = 10


class PaddleRight(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)


class PaddleLeft(PaddleRight):

    def __init__(self, pos):
        super().__init__(position= pos)
        self.goto(x=-350, y=0)



