from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json




# ---------------------------- Search Account ------------------------------- #
def find_password():
    #Grab website input
    website = web_input.get()


    if len(website) > 0:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
                user_info = data[website]
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Data File was not found")
        except KeyError as error_message:
            messagebox.showerror(title="Error", message=f"The key {error_message} was not found")
        else:
            messagebox.showinfo(title=website, message=f"Email: {user_info['email']}\n Password: {user_info['password']}")
    else:
        messagebox.showerror(title="Error", message="Website field left blank")






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
    new_data = {
        website: {
            "email": email,
            "password":password,
        }
    }

    if len(website) == 0 and len(password) == 0:
        msg = messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open ("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
            #Updating old data with new data
        else:
            data.update(new_data)


        with open("data.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)
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
web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()

email_input = Entry(width=21)
email_input.grid(row=2, column= 1)
email_input.insert(0, "test@gmail.com")

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

#Buttons
generate_pw_btn = Button(text="Generate Password", command=generate_password)
generate_pw_btn.grid(row=3, column=2)

search_btn = Button(text="Search", command=find_password, width=14)
search_btn.grid(row=1, column=2)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()