from turtle import Turtle


class ScoreBoard(Turtle):

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_board()

        # score controller for the left player
    def control_score_l(self):
        # self.clear()
        self.l_score += 1
        self.update_board()

        # score controller for the left player
    def control_score_r(self):
        # self.clear()
        self.r_score += 1
        self.update_board()

    def ball_speed(self):
        current=self.speed()
        self.speed(current+10)
