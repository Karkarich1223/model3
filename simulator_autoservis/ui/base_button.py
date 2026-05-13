from tkinter import Button, messagebox


class BaseButton:
    def __init__(self, text, font, x, y, width, onClick):
        self.button = Button(text=text, font=font, activebackground='blue', activeforeground='white')
        self.button.place(x=x, y=y, width=width)
        self.button.bind('<Button-1>', lambda event: onClick())