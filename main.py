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
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("Pong")
        ball.bounce()


screen.exitonclick()
