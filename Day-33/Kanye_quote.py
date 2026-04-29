from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Quote")
window.config(padx=50, pady=50)

canvas = Canvas(width=600, height=800)
background_img = PhotoImage(file="Day-33/background.png")
canvas.create_image(300, 400, image=background_img)
quote_text = canvas.create_text(300,400, text="Quote will be appear here", width= 280, font=("Arial", 30, "bold"), fill="White")
canvas.grid(row=0, column= 0)


kanye_img = PhotoImage(file="Day-33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()