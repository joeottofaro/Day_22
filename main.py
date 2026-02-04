import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle = Paddle()

screen.onkeypress(paddle.up_p1, "Up")
screen.onkeypress(paddle.down_p1, "Down")
screen.onkeypress(paddle.up_p2, "w")
screen.onkeypress(paddle.down_p2, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
