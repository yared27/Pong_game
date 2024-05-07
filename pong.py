# Define the positions for the paddles along the y-axis
POSITION = [(0,0),(0,50),(0,100),(0,150),(0,200),(0,250),(0,-50),(0,-100),(0,-150),(0,-200),(0,-250)]

# Define the positions for the top and bottom walls of the game area
POSITION1 = [(475,0),(475,20),(475,-20),(-480,0),(-480,20),(-480,-20)]

from turtle import Turtle

class Pong:
    def create(self):
        """
        Create the paddles for the Pong game.

        Each paddle is a Turtle object representing a segment of the paddle.

        """
        for i in range(0,11):
            self.turtle = Turtle("square")
            self.turtle.penup()
            self.turtle.color("white")
            self.turtle.color()
            self.turtle.goto(POSITION[i])

    def __init__(self):
        """
        Initialize the Pong game.

        This method creates the paddles using the create method.

        """
        self.create()
