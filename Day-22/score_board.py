from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()

    def left_score_board(self):
        self.goto(-200,270)
        self.write(f"Current score {self.score}", move= False, align="left", font=("Arial", 24,"normal")) 

    def right_score_board(self):
        self.goto(200,270)
        self.write(f"Current score {self.score}", move= False, align="right", font=("Arial", 24,"normal")) 



    def increase_score_left_board(self):
        self.score += 1
        self.clear()
        self.left_score_board()

    def increase_score_right_board(self):
        self.score += 1
        self.clear()
        self.right_score_board()



        
    def drawing_center_line(self):
        start_x = 0
        start_y = 300
        middle_line = Turtle()
        middle_line.shape("square")
        middle_line.turtlesize(stretch_wid=0.5, stretch_len=0.3)
        middle_line.color("white")


        while middle_line.ycor() >= -300:
            middle_line.penup()
            middle_line.goto(start_x, start_y)
            start_y -= 10
            middle_line.pendown()
            middle_line.goto(start_x, start_y)
            start_y -= 10


        



        

