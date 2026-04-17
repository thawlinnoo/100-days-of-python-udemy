from turtle import Turtle


class Snake:

    def __init__(self):
        self.all_block = []
        self.create_snake()
        

    def create_snake(self):
        
        x = 0
        y = 0
        for block in range(3):
            new_block = Turtle("square")
            new_block.penup()
            new_block.color("white")
            new_block.goto(x, y)   
            x -= 20
            self.all_block.append(new_block)

    def move(self):
    
        for blocks in range(len(self.all_block)-1, 0, -1):  
            front_block_x_cor = self.all_block[blocks-1].xcor()
            front_block_y_cor = self.all_block[blocks-1].ycor()
            self.all_block[blocks].goto(front_block_x_cor, front_block_y_cor)
        self.all_block[0].forward(20)

    def up(self):
        if self.all_block[0].heading() != 270:
            self.all_block[0].setheading(90)

    def down(self):
        if self.all_block[0].heading() != 90:
            self.all_block[0].setheading(270)

    def left(self):
        if self.all_block[0].heading() != 0:
            self.all_block[0].setheading(180)

    def right(self):
        if self.all_block[0].heading() != 1800:
            self.all_block[0].setheading(0)

