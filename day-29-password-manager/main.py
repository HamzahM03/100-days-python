# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

#Create Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Convert logo.png to an image available for use in Canva
pw_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=pw_logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

#Entries
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(row=2, column= 1, columnspan=2)

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

#Buttons
generate_pw_btn = Button(text="Generate Password")
generate_pw_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()