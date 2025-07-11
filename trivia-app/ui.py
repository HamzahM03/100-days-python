from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #Create score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row = 0, column=1)

        #Create a white canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column = 0, columnspan=2, pady=20 )

        #Insert questions onto the canvas
        self.question_text = self.canvas.create_text(
            150,  # x-position (center of the canvas)
            125,  # y-position (center of the canvas)
            text="Question goes here",  # Your question string
            fill="black",  # Text color
            font=("Arial", 20, "italic"),
            width=280  # Optional: wrap text nicely
        )

        # Load images (must be PNG or GIF)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # True Button
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # False Button
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)









        self.window.mainloop()