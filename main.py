import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))


screen.onkeypress(player_1.go_up, "Up")
screen.onkeypress(player_1.go_down, "Down")
screen.onkeypress(player_2.go_up, "w")
screen.onkeypress(player_2.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
