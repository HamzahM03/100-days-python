# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

#Create Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Convert logo.png to an image available for use in Canva
pw_logo = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100,100, image=pw_logo)
canvas.grid()


window.mainloop()