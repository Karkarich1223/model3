from tkinter import *
from tkinter import messagebox


def move(event):
    key = event.keysym

    home_coord = canva.coords(home)
    sova_coord = canva.coords(sova)

    if sova_coord[0] >= home_coord[0]+50 and 150 <= sova_coord[1]+50 <= 170:
        messagebox.showinfo("готово","Сова дома!")

    if key == "Up":
        canva.move(sova, 0, -10)
    elif key == "Down":
        canva.move(sova, 0, 10)
    elif key == "Left":
        canva.move(sova, -10, 0)
    elif key == "Right":
        canva.move(sova, 10, 0)
        
        
window = Tk()
window.geometry("700x700")
canva = Canvas(window, width=600, height=600, bg="lightblue")
canva.pack()
image = PhotoImage(file="test.png")
sova = canva.create_image(300, 300, image=image)
home=canva.create_rectangle(400, 150, 600,200, fill='brown')
window.bind("<KeyPress>", move)
window.mainloop()
