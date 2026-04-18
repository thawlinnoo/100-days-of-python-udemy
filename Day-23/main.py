import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()
score_board.level_board()


screen.onkey(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_creating()
    car_manager.move_car()
    if player.ycor() >= 300:
            player.reset_position()
            car_manager.increase_speed()
            score_board.increase_level()
    for i in car_manager.all_car_list:
        if player.distance(i) < 30:
            game_is_on = False
            score_board.game_over_board()
    
            
    



    



screen.exitonclick()
    
