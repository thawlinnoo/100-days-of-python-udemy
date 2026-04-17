# drawing with turtle

# from turtle import Turtle, Screen

# def clear_screen():
#     tim.clear()

# def reset_screen():
#     tim.reset()

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_right():
#     tim.right(10)

# def turn_left():
#     tim.left(10)

# tim = Turtle()
# screen = Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="r", fun=reset_screen)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)

# screen.exitonclick()
# -----------------------------------------------

#Final project

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle gonna win? Enter a color: ")
colors = ["red", "orange", "yellow", "black", "blue", "purple"]
all_turtle = []


x = -230
y = -100

for turtles in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>=230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You have won the race. The winning turtle is {winning_turtle}")
            else:
                print(f"You have lost the race. The winning turtle is {winning_turtle}")
        else:
            turtle.forward(random.randint(0,10))




screen.exitonclick()

