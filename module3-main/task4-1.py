from tkinter import *

def move(event):
    key = event.keysym
    if key == "Up":
        canva.move(sova, 0, -10)
    elif key == "Down":
        canva.move(sova, 0, 10)
    elif key == "Left":
        canva.move(sova, -10, 0)
    elif key == "Right":
        canva.move(sova, 10, 0)

window = Tk()
window.geometry("600x600")

canva = Canvas(window, width=600, height=600,bg="lightblue")
canva.pack()

image = PhotoImage(file = "test.png")
sova = canva.create_image(300, 300, image = image)

window.bind("<KeyPress>", move)

window.mainloop()