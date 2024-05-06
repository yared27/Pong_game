from turtle import Screen
from pong import Pong
from paddle_side import Paddle
from ball import Ball
from scorebored import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
pong = Pong()
score_bord = ScoreBoard()


paddle_l = Paddle((-370, 0))
paddle_r = Paddle((370, 0))

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")
is_game_on = True
ball = Ball()
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_move_speed)
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    # (paddle_l.xcor() - ball.xcor()==1 and paddle_r.ycor()-ball.ycor()==5 )or (paddle_r.xcor() - ball.xcor()==1 and paddle_l.ycor()-ball.ycor()==5)
    if (paddle_l.distance(ball)<50 and ball.xcor()<-340)or(paddle_r.distance(ball)<50 and ball.xcor()>340):
        score_bord.ball_speed()
        ball.bounce_x()
  #detect if the right paddle is misssed
    if ball.xcor()>380:
        score_bord.control_score_l()
        ball.reset_position()
  #detect if  the left paddle is missed
    if ball.xcor()<-380:
        score_bord.control_score_r()
        ball.reset_position()

# screen.mainloop()
screen.exitonclick()