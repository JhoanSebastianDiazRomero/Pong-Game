from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

scoreboard = Scoreboard()

game_is_one = True
while game_is_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with board
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
