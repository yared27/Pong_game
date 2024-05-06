POSITION=[(0,0),(0,50),(0,100),(0,150),(0,200),(0,250),(0,-50),(0,-100),(0,-150),(0,-200),(0,-250)]
POSITION1=[(475,0),(475,20),(475,-20),(-480,0),(-480,20),(-480,-20)]
from turtle import Turtle
class Pong:
    def create(self):
        for i in range(0,11):
            self.turtle = Turtle("square")
            self.turtle.penup()
            self.turtle.color("white")
            self.turtle.color()
            self.turtle.goto(POSITION[i])


    def __init__(self):
        # super().__init__()
        self.create()
        # self.paddle = Turtle("square")


