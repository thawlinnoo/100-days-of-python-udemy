from tkinter import *
from tkinter import messagebox #it need to import again because it is not class...
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    
    password_list += [choice(symbols) for char in range(randint(2, 4))]

    password_list += [choice(numbers) for char in range(randint(2, 4))]



    shuffle(password_list)


    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    web_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()

    if len(web_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showwarning(title="Oops", message="You cannot leave the field empty")

    
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entered: \nEmail: {email_name} \nPassword: {password_name} \nIs it ok to save?")
    
    if is_ok:

        with open ("Day-29/data.txt", "a") as file:
            file.write(f"{web_name} | {email_name} | {password_name}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)





# ---------------------------- UI SETUP ------------------------------- #




window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="Day-29/logo.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column=1, row=0)


label_1 = Label(text="Website" , font=("Arial", 20, "bold"))
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:" , font=("Arial", 20, "bold"))
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:" , font=("Arial", 20, "bold"))
label_3.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus() #the cursor will start there as soon as it is run

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "thaw@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

button_1 = Button(text="Generate Password", command=generate_password)
button_1.grid(column=2, row=3)

button_2 = Button(text="Add", width=33, command=save_password)
button_2.grid(column=1, row=4, columnspan=2)


window.mainloop()



