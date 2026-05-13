from tkinter import *
import random

window = Tk()
canva = Canvas(width=640, height=640, bg='lightblue')
canva.pack()


colors = [
    'red', 'blue', 'green', 'yellow', 'purple', 'orange',
    'pink', 'cyan', 'magenta', 'lime', 'gold', 'silver',
    'brown', 'turquoise', 'violet', 'skyblue'
]

class Ball:
    def __init__(self, canvas, colors_list):
        self.canvas = canvas
        self.x = random.randint(20, 620)
        self.y = random.randint(20, 620)
        self.r = 20
        self.color = random.choice(colors_list)
        colors_list.remove(self.color)

        self.id = self.canvas.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=self.color
        )

        self.vx = random.choice([-10, 10, -15, 15])
        self.vy = random.choice([-10, 10, -15, 15])
        print(self.color)

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)

        if x1 <= 0 or x2 >= 640:
            self.vx *= -1

        if y1 <= 0 or y2 >= 640:
            self.vy *= -1

        self.canvas.move(self.id, self.vx, self.vy)


balls = []
color_list = colors.copy()

for _ in range(15):
    ball = Ball(canva, color_list)
    balls.append(ball)

def animate():
    for b in balls:
        b.move()
    canva.after(50, animate)

animate()
window.mainloop()