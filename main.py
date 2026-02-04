import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(player_1.go_up, "Up")
screen.onkeypress(player_1.go_down, "Down")
screen.onkeypress(player_2.go_up, "w")
screen.onkeypress(player_2.go_down, "s")


def play_pong():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # Detect collision with paddle
        if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        # Detect if player 1 missed the ball
        if ball.xcor() < -380:
            ball.reset_ball()
            scoreboard.player_2_point()
        # Detect if player 2 missed the ball
        if ball.xcor() > 380:
            ball.reset_ball()
            scoreboard.player_1_point()
        # Winning
        if scoreboard.player_1_score == 10 or scoreboard.player_2_score == 10:
            scoreboard.winner()
            game_is_on = False
            play_again = screen.textinput("Another game","Type yes to play again.")
            if play_again == "yes":
                scoreboard.clear_score()
                play_pong()
            else:
                exit()


play_pong()
screen.exitonclick()
