from tkinter import *
import pandas
import random

#CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# Manually constructed dict from columns (just for fun)
# new_dict = {data_dict["French"][i] : data_dict["English"][i] for i in range(len(data_dict["French"]))}
# print(new_dict)

#Read data from french_words.csv
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")



#-------------------------GENERATE A RANDOM WORD TO DISPLAY-----------------------------
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])






#Create window
window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#create card image to put on canvas representing the front of the card
card_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

#Text on canvas
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME,40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME,60, "bold"))

#Buttons
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_btn = Button(image=incorrect_img, highlightthickness=0, command=next_card)
incorrect_btn.grid(row=1, column=0)

correct_img = PhotoImage(file="images/right.png")
correct_btn = Button(image=correct_img, highlightthickness=0, command=next_card)
correct_btn.grid(row=1, column=1)


next_card()

window.mainloop()