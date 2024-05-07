from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Set the shape of the paddle
        self.color("white")   # Set the color of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust the size of the paddle
        self.penup()          # Lift the pen to avoid drawing lines
        self.goto(position)   # Move the paddle to the specified position

    def go_up(self):
        # Move the paddle up by 40 units
        y_cor = self.ycor() + 40
        self.goto(self.xcor(), y_cor)  # Update the position of the paddle
        self.screen.update()            # Update the screen to reflect the changes

    def go_down(self):
        # Move the paddle down by 40 units
        y_cor = self.ycor() - 40
        self.goto(self.xcor(), y_cor)  # Update the position of the paddle
        self.screen.update()            # Update the screen to reflect the changes
