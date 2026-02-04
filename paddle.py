from turtle import Turtle

WIDTH = 1
HEIGHT = 5
STARTING_POSITIONS = [(350, 0), (-350, 0)]
UP = 90


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.player_1 = self.paddles[0]
        self.player_2 = self.paddles[1]

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_paddle(position)

    def add_paddle(self, position):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        new_paddle.goto(position)
        self.paddles.append(new_paddle)

    def up_p1(self):
        new_y = self.player_1.ycor() + 20
        self.player_1.goto(self.player_1.xcor(), new_y)

    def down_p1(self):
        new_y = self.player_1.ycor() - 20
        self.player_1.goto(self.player_1.xcor(), new_y)

    def up_p2(self):
        new_y = self.player_2.ycor() + 20
        self.player_2.goto(self.player_2.xcor(), new_y)

    def down_p2(self):
        new_y = self.player_2.ycor() - 20
        self.player_2.goto(self.player_2.xcor(), new_y)
