import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()

screen.onkeypress(player_1.go_up, "Up")
screen.onkeypress(player_1.go_down, "Down")
screen.onkeypress(player_2.go_up, "w")
screen.onkeypress(player_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect if player 1 missed the ball
    if ball.xcor() > 380:
        ball.reset_ball()

    # Detect if player 2 missed the ball
    if ball.xcor() < -380:
        ball.reset_ball()

screen.exitonclick()
