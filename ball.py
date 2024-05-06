from turtle import Turtle,Screen
from paddle_side import Paddle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.paddle=Paddle()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,0)
        self.x_move=20
        self.y_move=20
        self.ball_move_speed=0.2

    def bounce_y(self):
              self.y_move*=-1
    def bounce_x(self):
        self.x_move *= -1
        self.ball_move_speed*=0.9

    def move(self):
        # self.penup()
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

