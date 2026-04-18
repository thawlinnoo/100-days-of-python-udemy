from turtle import Turtle



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        
        




    def create_left_paddle(self):
        self.goto(-350,0)

    def create_right_paddle(self):
        self.goto(350,0)


    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
    

        


    # def move(self):
    #     self.up()
    #     self.forward(20)

    # def up(self):
    #     self.setheading(90)
    
    # def down(self):
    #     self.setheading(270)

    


    










