from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from midline import Midline
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

paddle_r = Paddle((350, 0), "Up", "Down")
paddle_l = Paddle((-350, 0), "w", "s")
ball = Ball()

scoreboard = Scoreboard()
midline = Midline()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50:
        ball.bounce_off_paddle()

    elif ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_off_paddle()

    # detect if it goes past right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if it goes past left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
