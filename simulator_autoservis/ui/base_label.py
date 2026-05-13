from tkinter import Label


class BaseLabel:
    def __init__(self, text, font, bg,x,y):
        self.label = Label(text=text, font=font, bg=bg)
        self.label.place(x=x, y=y)