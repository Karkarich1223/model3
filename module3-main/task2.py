from tkinter import *
import random
from tkinter import messagebox

window = Tk()

window.geometry('500x500')
canva = Canvas(width=500, height=500, bg="Lightgreen")
canva.pack()


balls = [
    canva.create_oval(50, 50, 100, 100, fill='white'),
    canva.create_oval(50, 150, 100, 200, fill='blue'),
    canva.create_oval(50, 250, 100, 300, fill='red')
]

after_id = None

def start():
    if after_id:
        canva.after_cancel(after_id)
    for ball in balls:
        canva.coords(ball, canva.coords(ball)[0], canva.coords(ball)[1], canva.coords(ball)[2], canva.coords(ball)[3])
    start()

def again():
    if after_id:
        canva.after_cancel(after_id)
    canva.coords(balls[0], 50, 50, 100, 100)
    canva.coords(balls[1], 50, 150, 100, 200)
    canva.coords(balls[2], 50, 250, 100, 300)
    start()

def start():
    for ball in balls:
        step = random.randint(1, 20)
        canva.move(ball, step, 0)
        if canva.coords(ball)[2] >= 500:
            winner_color = canva.itemcget(ball, 'fill')
            messagebox.showinfo("Victory", f"{winner_color} ball was win")
            after_id = None
            return
    after_id = canva.after(50, start)

btn_start = Button(text="Start", font="Arial 15", command=start)
btn_start.place(x=190, y=400)

btn_return = Button(text="Return", font="Arial 15", command=again)
btn_return.place(x=260, y=400)

window.mainloop()