from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")
screen.listen()




snake = Snake()
food = Food()
score_board = Score_board()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #detect the eating 
    if snake.all_block[0].distance(food)<15:
        food.refresh()
    
    #score board
        score_board.increase_score()

    #extend the snake after eating
        snake.extend()

    #Detect collision with wall
    if snake.all_block[0].xcor() > 290 or snake.all_block[0].xcor() < -290 or snake.all_block[0].ycor() >290 or snake.all_block[0].ycor() < -290:
        game_on = False
        score_board.game_over()
        

    #Detect collision with tail(any block from body)
    for blocks in snake.all_block[1:]:       # (slicing, so it will only check starting from index 1 to the end.. skip the head block)
        if snake.all_block[0].distance(blocks) < 10:
            game_on = False
            score_board.game_over()


    


          

screen.exitonclick()