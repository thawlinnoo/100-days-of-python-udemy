BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas




picking_random_word_index = None
flip_timer = None
try:
    data = pandas.read_csv("Day-31/data/words_to_learn.csv")  
except FileNotFoundError:
    data = pandas.read_csv("Day-31/data/french_words.csv")
data_dict = data.to_dict(orient="records")





# ------------------------ Display french word on flashcard --------------------------
def display_french():
    canvas.itemconfig(french_img, image=front_img)
    random_french_word = data_dict[picking_random_word_index]["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_french_word, fill="black")

# ------------------------ Display english word on flashcard --------------------------

def display_english():
    canvas.itemconfig(french_img, image=back_img)
    random_english_word = data_dict[picking_random_word_index]["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_english_word, fill="white")

# ------------------------ pick card and remove known word from list --------------------------



def next_card():
    global flip_timer
    global picking_random_word_index
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    if len(data_dict) == 0:
        canvas.itemconfig(title, text="Done")
        canvas.itemconfig(word, text="")
        return
    picking_random_word_index = random.randint(0,len(data_dict)-1)
    display_french()
    flip_timer = window.after(3000, display_english)

# ------------------------ remove known word from list --------------------------

def remove_word():
    if picking_random_word_index is not None:
        data_dict.remove(data_dict[picking_random_word_index])
        data = pandas.DataFrame(data_dict)
        data.to_csv("Day-31/data/words_to_learn.csv", mode="w", index=False)
    next_card()
    

# ------------------------ UI --------------------------

window = Tk()
window.title("Flashy")

window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

canvas= Canvas(width=800, height=526)
front_img = PhotoImage(file="Day-31/images/card_front.png")
back_img = PhotoImage(file="Day-31/images/card_back.png")
french_img = canvas.create_image(400, 263, image=front_img)
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness = 0)
title = canvas.create_text(400,150, text="Title", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400,263, text="word", fill="black", font=("Arial", 60, "bold"))


canvas.grid(column=0,row=0, columnspan=2)



wrong_img = PhotoImage(file="Day-31/images/wrong.png")
button_1 = Button(image=wrong_img, highlightthickness=0, command = next_card)
button_1.grid(column=0, row=1)

right_img = PhotoImage(file="Day-31/images/right.png")
button_2 = Button(image=right_img, highlightthickness=0, command=remove_word)
button_2.grid(column=1, row=1)



window.mainloop()
             
             
             
             
             




