from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters      # a-z + A-Z
    digits = string.digits              # 0-9
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"

    # Choose how many characters of each type
    password_letters = [random.choice(letters) for _ in range(6)]
    password_digits = [random.choice(digits) for _ in range(2)]
    password_symbols = [random.choice(symbols) for _ in range(2)]

    # Combine and shuffle
    password_list = password_letters + password_digits + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    # Insert into the password entry field
    pw_input.delete(0, END)
    pw_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = web_input.get()
    email = email_input.get()
    password = pw_input.get()

    if len(website) == 0 and len(password) == 0:
        msg = messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_ok:
            with open ("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, END)
                pw_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #


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
web_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column= 1, columnspan=2)
email_input.insert(0, "test@gmail.com")

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

#Buttons
generate_pw_btn = Button(text="Generate Password", command=generate_password)
generate_pw_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()