from turtle import Turtle


with open("Day-20, 21, 24/data.txt", "r") as file:
    content = file.read()

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(content)
        self.color("white") 
        self.penup() 
        self.goto(0, 270) 
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Current score: {self.score}.  High score: {self.high_score}", move= False, align="center", font=("Arial", 24,"normal"))  

    def increase_score(self):       
        self.score += 1
        self.update_score()

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day-20, 21, 24/data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, "center", ("Arial", 24,"normal"))
        

