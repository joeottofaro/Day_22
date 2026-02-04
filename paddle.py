from turtle import Turtle

WIDTH = 1
HEIGHT = 5


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        xy_pos = starting_position
        self.paddle = self.create_paddle(xy_pos)

    def create_paddle(self, position):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        new_paddle.goto(position)
        return new_paddle

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)