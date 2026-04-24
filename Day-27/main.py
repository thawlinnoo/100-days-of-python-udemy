


#--------------------------


# #unlimited arguments
# # u can use args as the tuple... for example  args[1]
# def add(*args): 
#     total = 0
#     for n in args:
#         total += n
#     print(total)
# add(2,3,4,5,6)

# # u can use kwargs as dict.. for example kwargs["add"] which will return 3
# def calculate (**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)

# calculate(add=3, multiply=5)


#---------------------------

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make") # use method "get" so it own't give error and will just return "none" for un specify arguments
#         self.model = kwargs.get("model")

# my_car = Car(make="germany")
# print(my_car.make, my_car.model) 

#--------------------------- 


from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100) #space between around it..

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack() # # require this line to appear on screen and can choose side to appear here
my_label.grid(column=0, row=0)

# my_label["text"] = "new text 1"
# my_label.config(text="new text 2")

def button_clicked():
   
    my_label.config(text=my_entry.get())

my_button = Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

my_button_2 = Button(text="Click me 2", command=button_clicked)
# my_button.pack()
my_button_2.grid(column=2, row=0)

my_entry = Entry(width=10)
# my_entry.pack()
# my_entry.place(x=100,y=200) #place on specific xcor ycor
my_entry.grid(column=3, row=3) #place on specific column row
# my_entry.get() # this line return the str that i type into the entry box


window.mainloop()
