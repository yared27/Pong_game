from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")          # Set the shape of the ball
        self.color("blue")            # Set the color of the ball
        self.penup()                  # Lift the pen to avoid drawing lines
        self.goto(0, 0)               # Move the ball to the center of the screen
        self.x_move = 20              # Set the initial x-axis movement of the ball
        self.y_move = 20              # Set the initial y-axis movement of the ball
        self.ball_move_speed = 0.2    # Set the initial speed of the ball

    def bounce_y(self):
        # Reverse the direction of movement along the y-axis
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the direction of movement along the x-axis
        self.x_move *= -1
        # Decrease the speed of the ball to simulate friction
        self.ball_move_speed *= 0.9

    def move(self):
        # Move the ball by the specified x_move and y_move values
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def reset_position(self):
        # Reset the position of the ball to the center of the screen
        self.goto(0, 0)
        # Reverse the direction of movement along the x-axis
        self.bounce_x()
