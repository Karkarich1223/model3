import tkinter as tk
import random

window = tk.Tk()
window.title("СНЕГОПАД")
window.geometry("600x600")

canvas = tk.Canvas(window, width=600, height=600, bg="lightblue")
canvas.pack()

image = tk.PhotoImage(file="snow.png")
snow_flake_speed = 5
snow_flakes = []

def spawn_snowflake():
    create_snowflake()
    window.after(2000, spawn_snowflake)

def create_snowflake():
    x = random.randint(0, 600)
    y = 0

    snowflake = canvas.create_image(x, y, image=image, anchor='nw')

    snow_flakes.append(snowflake)
    move_snowflake(snowflake)

def move_snowflake(snowflake):
    x, y = canvas.coords(snowflake)

    canvas.move(snowflake, 0, snow_flake_speed)

    y += snow_flake_speed

    if y < 600:
        window.after(50, move_snowflake, snowflake)
    else:
        canvas.delete(snowflake)
        if snowflake in snow_flakes:
            snow_flakes.remove(snowflake)
        create_snowflake()
spawn_snowflake()

window.mainloop()