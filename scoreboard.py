from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.player_1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player_2_score, align="center", font=("Courier", 80, "normal"))

    def player_1_point(self):
        self.player_1_score += 1
        self.clear()
        self.update_score()

    def player_2_point(self):
        self.player_2_score += 1
        self.clear()
        self.update_score()
