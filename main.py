from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

p1_x = 350
p1_y = 0
p2_x = -350
p2_y = 0

paddle = Paddle()

player_1 = paddle.player_1
player_2 = paddle.player_2

screen.onkeypress(paddle.up_p1, "Up")
screen.onkeypress(paddle.down_p1, "Down")
screen.onkeypress(paddle.up_p2, "w")
screen.onkeypress(paddle.down_p2, "s")

screen.exitonclick()
