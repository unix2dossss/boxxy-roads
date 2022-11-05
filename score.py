from turtle import Turtle
FONT = ("Verdana", 10, "normal")
SCORE_Y_COORD = 275
SCORE_X_COORD = 250


class playerScore(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_score()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_score()

    def update_score(self):
        self.hideturtle()
        self.penup()
        self.setpos(SCORE_X_COORD, SCORE_Y_COORD)
        self.color("white")
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def reset_score(self):
        self.level = 0
        self.clear()
        self.update_score()
