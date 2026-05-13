from tkinter import *
def click_function(event):
    canva.itemconfig('blue_rect', fill='red')
    canva.itemconfig('black_rect', fill='green')
    canva.itemconfig('yellow_rect', fill='blue')


window = Tk()
window.geometry("500x500")

canva = Canvas(width=500, height = 500, bg = "Lightgreen")
canva.pack()

rect1 = canva.create_rectangle(50, 50, 100, 100, fill = "blue", tags = ('rect', 'blue_rect'))
rect2 = canva.create_rectangle(50, 150, 100, 200, fill = "blue", tags = ('rect', 'yellow_rect'))
rect3 = canva.create_rectangle(50, 250, 100, 300, fill = "blue", tags = ('rect', 'black_rect'))

canva.tag_bind('rect', '<Button-1>', click_function)

window.mainloop()