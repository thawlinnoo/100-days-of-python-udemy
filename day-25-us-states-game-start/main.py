from turtle import Turtle, Screen
import pandas
import time

screen = Screen()
screen.tracer(0)
turtle = Turtle()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
on_map_letter = Turtle()
on_map_letter.hideturtle()
on_map_letter.penup()
on_map_letter.goto(-100,200)
score_board = Turtle()
score_board.penup()
score_board.hideturtle()
score_board.goto(100,230)
corrected_guesses = []
all_states = data.state.to_list()
score = 0






while len(corrected_guesses) < 50:
    screen.update() 
    time.sleep(0.1)
    answer = screen.textinput(title= "Guess the state", prompt= " What's another state's name?: ")
    
    format_answer = answer.title()

    if format_answer == "Exit":
        break
        
   
    

    if (data.state == format_answer).any() and format_answer not in corrected_guesses:

        corrected_guesses.append(format_answer)
        score += 1
        
        x_cor = data[data.state == format_answer].x.item()
        y_cor = data[data.state == format_answer].y.item()

        on_map_letter.goto(x_cor, y_cor)
        on_map_letter.write(format_answer, font=("Arial", 12, "bold"), align="center")
        
        score_board.clear()
        score_board.write(f"Current score: {score}", font=("Arial", 15, "bold"), align="center")
   
        

missing_states = [states for states in all_states if states not in corrected_guesses]


data_dict = {
    "Missing States" : missing_states
}
New_csv = pandas.DataFrame(data_dict)
New_csv.to_csv("day-25-us-states-game-start/Missing_state.csv")





    
    
        
        




screen.mainloop()