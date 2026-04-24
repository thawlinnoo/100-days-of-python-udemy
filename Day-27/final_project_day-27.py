from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=250)
window.config(padx=75, pady=80)

def convert():
    miles = my_entry.get()
    km = round(float(miles) * 1.60934, 2)
    answer_label.config(text=km)



label_2 = Label(text="is equal to", font=("Arial", 24, "bold"))
label_2.grid(column=0, row=1)

my_entry = Entry(width=15, font=("Arial", 24, "bold"))
my_entry.grid(column=1, row=0)

answer_label = Label(text="0", font=("Arial", 24, "bold"))
answer_label.grid(column=1, row=1)

my_button = Button(text="Calculate", font=("Arial", 24, "bold"), command=convert)
my_button.grid(column=1,row=2)

label_3 = Label(text="Miles", font=("Arial", 24, "bold"))
label_3.grid(column=2, row=0)

label_4 = Label(text="Km", font=("Arial", 24, "bold"))
label_4.grid(column=2, row=1)



window.mainloop()