from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

        


 
    def car_creating(self):
        create_chance = random.randint(1,6)
        if create_chance == 6:
            cars = Turtle()
            cars.shape("square")
            cars.turtlesize(stretch_wid=1, stretch_len=2)
            cars.penup()
            cars.color(random.choice(COLORS))
            cars.goto(300, random.randint(-245,245))
            self.all_car_list.append(cars)

    def move_car(self):
        for cars in self.all_car_list:
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        


        
            


            









