from tkinter import *
window = Tk()
window.geometry("400x400")

def move(event):
    x, y = event.x, event.y
    x1, y1, x2, y2 = canvas.coords(ball)
    # print("x=",x,"y=",y)

    if x > 80 and y > 30 and x < 320 and y < 370:
        canvas.coords(ball, x-25, y-25,x+25,y+25)


canvas = Canvas(window, width=400, height=400,bg="lightblue")
canvas.pack()

ball = canvas.create_oval(150, 50, 200, 100, fill = "red")
canvas.bind("<Motion>", move)

wall = canvas.create_rectangle(80,30,320,370)

window.mainloop()