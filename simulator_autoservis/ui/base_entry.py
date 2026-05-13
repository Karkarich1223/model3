from tkinter import StringVar, Entry

class BaseEntry:
    def __init__(self, font, x, y, width, mask):
        self.value = StringVar()
        if mask == True:
            show = "*"
        else:
            show = ""
        self.entry = Entry(textvariable=self.value, font=font, show=show)
        self.entry.place(x=x, y=y, width=width)