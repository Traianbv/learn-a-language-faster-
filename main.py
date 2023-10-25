BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

curent_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/german.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # for arange the dict



def next_card():
    global curent_card,flip_timer
    window.after_cancel(flip_timer)
    curent_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=curent_card["German"], fill="black")
    canvas.itemconfig(card_background, image=image_bg)
    flip_timer = window.after(4000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curent_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def know_card():
    to_learn.remove(curent_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flip_card)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
image_bg = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(450, 300, image=image_bg)
card_title = canvas.create_text(430, 200, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(430, 300, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

# button cross
no_ok = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=no_ok, command=next_card)
button_wrong.grid(column=0, row=1)

# button ok
ok_mark = PhotoImage(file="images/right.png")
button_ok = Button(image=ok_mark, command=know_card)
button_ok.grid(column=1, row=1)

# read file
next_card()

window.mainloop()
