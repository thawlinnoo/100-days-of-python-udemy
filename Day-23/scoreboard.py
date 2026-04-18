from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.color("white")
        self.hideturtle()

    def level_board(self):
        self.goto(-200,260)
        self.write(f"Level: {self.level}", move= False, align="left", font=FONT)

    def game_over_board(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", move= False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.level_board()

    
