# Import necessary modules
from turtle import Screen
from pong import Pong
from paddle_side import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Set up the game screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create instances of game objects
pong = Pong()
score_board = ScoreBoard()
paddle_l = Paddle((-370, 0))
paddle_r = Paddle((370, 0))

# Listen for keyboard inputs
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

# Set up the game loop
is_game_on = True
ball = Ball()
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_move_speed)

    # Detect if the ball hits the top or bottom wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect if the ball hits a paddle and adjust its speed
    if (paddle_l.distance(ball) < 50 and ball.xcor() < -340) or (paddle_r.distance(ball) < 50 and ball.xcor() > 340):
        score_board.ball_speed()
        ball.bounce_x()

    # Detect if the ball is missed by the right paddle
    if ball.xcor() > 380:
        score_board.control_score_l()
        ball.reset_position()

    # Detect if the ball is missed by the left paddle
    if ball.xcor() < -380:
        score_board.control_score_r()
        ball.reset_position()

# Exit the game when clicking on the screen
screen.exitonclick()
