from tkinter import *
from tkinter import simpledialog
import pandas
import random
import time
import os



#CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}


# Manually constructed dict from columns (just for fun)
# new_dict = {data_dict["French"][i] : data_dict["English"][i] for i in range(len(data_dict["French"]))}
# print(new_dict)



#-------------------------GENERATE A RANDOM WORD TO DISPLAY-----------------------------
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Arabic", fill="black")
    canvas.itemconfig(card_word, text=current_card["Levantine Arabic (Transliterated)"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    window.after(3000, flip_card)


#-------------------------FLIP CARD-----------------------------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


#-------------------------Remove Known Cards and save remaining words to csv file to save progress-----------------------------
def known_card():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv(progress_file, index=False)
    next_card()

#-------------------------Reset Progress-----------------------------
def reset_progress():
    global to_learn
    data = pandas.read_csv(base_file)
    to_learn = data.to_dict(orient="records")
    pandas.DataFrame(to_learn).to_csv(progress_file, index=False)
    next_card()



#Create window
window = Tk()
window.title("Learn Arabic")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Ask user what difficulty of arabic they want to learn
difficulty = simpledialog.askstring("Difficulty", "Choose difficulty: beginner, intermediate, or expert").lower()
base_file = f"data/Arabic/arabic_{difficulty}.csv"
progress_file = f"data/Arabic/{difficulty}_arabic_words_to_learn.csv"

#Read data from french_words.csv
if os.path.exists(progress_file):
    data = pandas.read_csv(progress_file)
else:
    data = pandas.read_csv(base_file)
to_learn = data.to_dict(orient="records")



# Card images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

#Text on canvas
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME,40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME,50, "bold"))

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=known_card)
right_btn.grid(row=1, column=1)

#Reset Buttton
reset_btn = Button(text="Reset Progress", command=reset_progress, font=(FONT_NAME, 12, "bold"), bg="white", fg="black")
reset_btn.grid(row=2, column=0, columnspan=2, pady=20)




next_card()

window.mainloop()