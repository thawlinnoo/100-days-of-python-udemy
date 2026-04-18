from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time







screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()






left_paddle = Paddle()
left_paddle.create_left_paddle()
right_paddle = Paddle()
right_paddle.create_right_paddle()
ball = Ball()
left_score_board = Score_board()
left_score_board.left_score_board()
right_score_board = Score_board()
right_score_board.right_score_board()
middle_line = Score_board()
middle_line.drawing_center_line()





screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() > 320 and abs(ball.ycor() -  right_paddle.ycor()) < 50 :
        ball.bounce_paddle()

    if ball.xcor() < -320 and abs(ball.ycor() -  left_paddle.ycor()) < 50 :
        ball.bounce_paddle()

    if ball.xcor() > 400:
        left_score_board.increase_score_left_board()
        ball.reset_position()

    if ball.xcor() < -400:
        right_score_board.increase_score_right_board()
        ball.reset_position()



    














    


screen.exitonclick()

