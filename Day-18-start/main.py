from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")


# # making square
# for i in range(0,4):
#     tim.forward(100)
#     tim.right(90)

# # dash line
# for i in range (10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # making triangle to till decagon with random colors
# current_shape = 3
# while current_shape<=10:
#     tim.color(random.random(), random.random(), random.random())
#     for i in range(current_shape):
#         tim.forward(100)
#         tim.right(360/current_shape)
#     current_shape += 1

# # walking randomly
# direction = [0,90,180,270,360]
# going = True
# tim.pensize(15)
# tim.speed(10)
# for i in range(200):
#     tim.color(random.random(), random.random(), random.random())
#     tim.forward(50)
#     tim.setheading(direction[random.randint(0,4)])

# difference between tuple and list is tuple cannot be change or remove the item in that
# example tuple 
# my_tuple = (2,3,4)
# print(my_tuple[1])


# # another way to get random color by using rgb
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# tim.color(random_color())

# # making_spirograph
# tim.speed(0)
# def making_spirograph(gap_size):
#     for i in range(360//gap_size):
#         tim.color(random.random(), random.random(), random.random())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap_size)
# making_spirograph(5)



# final project
    
turtle.colormode(255)

color_list = [(204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123), 
              (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), 
              (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), 
              (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), 
              (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)
]

x = 0
y = 0
tim.setpos(x, y)
tim.hideturtle()
for dot in range(10):
    for dot in range(10):
        tim.pendown()
        tim.dot(20, color_list[random.randint(0,len(color_list)-1)])
        x += 25
        tim.penup()
        tim.setpos(x, y)
        
    x = 0
    y += 25
    tim.setpos(x, y)


    



screen = Screen()
screen.exitonclick()