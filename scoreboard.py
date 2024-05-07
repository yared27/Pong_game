from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()             # Hide the turtle icon
        self.color("white")           # Set the color of the text
        self.penup()                  # Lift the pen to avoid drawing lines
        self.l_score = 0              # Initialize the left player's score
        self.r_score = 0              # Initialize the right player's score
        self.update_board()           # Update the scoreboard with the initial scores

    def update_board(self):
        # Clear the previous scoreboard
        self.clear()
        # Write the left player's score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Write the right player's score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def control_score_l(self):
        # Increment the left player's score by 1
        self.l_score += 1
        # Update the scoreboard with the new score
        self.update_board()

    def control_score_r(self):
        # Increment the right player's score by 1
        self.r_score += 1
        # Update the scoreboard with the new score
        self.update_board()

    def ball_speed(self):
        # Increase the speed of the ball
        current_speed = self.speed()
        self.speed(current_speed + 10)
