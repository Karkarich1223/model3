from tkinter import *
import random

def click_function(event):
    while True:
        for i in range(16):
            color = random.choice(random_color)
            canva.itemconfig("ball"+str(i), fill=color)
            canva.update()
            canva.after(50)


window = Tk()

window.geometry('500x500')
canva=Canvas(width=500, height=500, bg="Lightgreen")
canva.pack()


random_color=['red','blue', 'green']

for i in range(16):
    color = random.choice(random_color)
    canva.create_oval(20+i*30, 50, 40+i*30, 70, fill=color, tags="ball"+str(i) )
canva.create_line(0,50,500,50)
canva.create_text(250,150,text="нажми для нового года", font="Arial 20", activefill="red", tags="start")
canva.tag_bind('start', "<Button 1>", click_function)


window.mainloop()