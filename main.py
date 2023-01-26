from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle1 and paddle 2
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if paddle1 missed
    if ball.xcor() > 380:
        ball.refresh()
        score.point2()

    # Detect if paddle2 missed
    if ball.xcor() < -380:
        ball.refresh()
        score.point1()


screen.exitonclick()
