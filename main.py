from turtle import Screen
from paddle import PaddleRight, PaddleLeft
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("pink")
screen.setup(width=800, height=600)

screen.title("Pong")
screen.tracer(0)

paddle_right = PaddleRight((350, 0))
paddle_left = PaddleLeft((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_paddle()
        scoreboard.l_update()

    if ball.xcor() < -380:
        ball.reset_paddle()
        scoreboard.r_update()

screen.exitonclick()
