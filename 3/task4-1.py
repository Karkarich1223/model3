from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.geometry("600x600")

canvas = Canvas(root, width=600, height=600, bg="lightblue")
canvas.pack()


home = canvas.create_rectangle(200, 100, 400, 150, fill="brown")

image = PhotoImage(file="test.png")
sova = canvas.create_image(300, 300, image=image)

def move(event):
    keysym = event.keysym
    if keysym == "Up":
        canvas.move(sova, 0, -10)
    elif keysym == "Down":
        canvas.move(sova, 0, 10)
    elif keysym == "Left":
        canvas.move(sova, -10, 0)
    elif keysym == "Right":
        canvas.move(sova, 10, 0)

    sova_coords = canvas.coords(sova)
    home_coords = canvas.coords(home)

    left, top, right, bottom = home_coords
    x, y = sova_coords[0], sova_coords[1]

    if left <= x <= right and top <= y <= bottom:
        msgbox.showinfo("Информация", "Сова дома!")

root.bind("<KeyPress>", move)
root.mainloop()