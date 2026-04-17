from turtle import Turtle




class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white") 
        self.penup() 
        self.goto(0, 270) 
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Current score {self.score}", move= False, align="center", font=("Arial", 24,"normal"))  

    def increase_score(self):       
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial", 24,"normal"))
        

