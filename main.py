# Модуль 3 - Все уроки в одном проекте
# Выберите урок для запуска внизу файла

import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
import random
import time
import sqlite3
import sys
import subprocess
import os


# ======================== УРОК 1: Анимация. Праздничная гирлянда ========================

def lesson_1_garland():
    def change_color():
        colors = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple", "pink"]
        for i in range(8):
            color = random.choice(colors)
            canva.itemconfig(f"oval{i}", fill=color)
        canva.update()
        canva.after(500, change_color)

    window = Tk()
    window.geometry("600x600")
    window.title("Праздничная гирлянда - Урок 1")

    canva = Canvas(window, width=600, height=600, bg="white")
    canva.pack()

    colors = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple", "pink"]
    for i in range(8):
        color = random.choice(colors)
        canva.create_oval(50 + i * 60, 200, 100 + i * 60, 250, fill=color, tags=f"oval{i}")

    canva.create_line(30, 225, 530, 225, width=3, fill="black")

    text = canva.create_text(300, 100, text="ЗАПУСТИТЬ ГИРЛЯНДУ",
                             font=("Arial", 20), fill="blue", activefill="red", tags="start")
    canva.tag_bind("start", "<Button-1>", lambda e: change_color())

    window.mainloop()


# ======================== УРОК 2: Анимация движения объектов ========================

def lesson_2_ball_race():
    def start_race():
        balls = [ball1, ball2, ball3, ball4]
        colors_balls = ["red", "blue", "green", "orange"]
        winner = None
        while not winner:
            for i, ball in enumerate(balls):
                step = random.randint(1, 20)
                canva.move(ball, step, 0)
                coords = canva.coords(ball)
                if coords[2] >= 500:
                    winner = colors_balls[i]
                    break
            canva.update()
            canva.after(50)
        messagebox.showinfo("Победитель", f"Победил {winner} шар!")

    window = Tk()
    window.geometry("600x400")
    window.title("Гонка шаров - Урок 2")

    canva = Canvas(window, width=600, height=400, bg="white")
    canva.pack()

    ball1 = canva.create_oval(20, 50, 70, 100, fill="red")
    ball2 = canva.create_oval(20, 120, 70, 170, fill="blue")
    ball3 = canva.create_oval(20, 190, 70, 240, fill="green")
    ball4 = canva.create_oval(20, 260, 70, 310, fill="orange")

    btn = Button(window, text="Старт", command=start_race)
    btn.pack()

    window.mainloop()


# ======================== УРОК 3: Движение и отталкивание объектов ========================

def lesson_3_bouncing_balls():
    class Ball:
        def __init__(self, canva):
            self.canva = canva
            x = random.randint(20, 580)
            y = random.randint(20, 580)
            color = random.choice(["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan"])
            self.ball = canva.create_oval(x, y, x + 30, y + 30, fill=color)
            self.vx = random.choice([-3, -2, 2, 3])
            self.vy = random.choice([-3, -2, 2, 3])

        def move(self):
            coords = self.canva.coords(self.ball)
            if coords[0] <= 0 or coords[2] >= 640:
                self.vx = -self.vx
            if coords[1] <= 0 or coords[3] >= 640:
                self.vy = -self.vy
            self.canva.move(self.ball, self.vx, self.vy)

    window = Tk()
    window.title("Прыгающие шары - Урок 3")

    canva = Canvas(window, width=640, height=640, bg="lightblue")
    canva.pack()

    balls = [Ball(canva) for _ in range(15)]

    def animation():
        for ball in balls:
            ball.move()
        canva.after(50, animation)

    animation()
    window.mainloop()


# ======================== УРОК 4: Управление движением объектов ========================

def lesson_4_mouse_control():
    window = Tk()
    window.geometry("400x400")
    window.title("Управление мышкой - Урок 4")

    canva = Canvas(window, width=400, height=400, bg="white")
    canva.pack()

    ball = canva.create_oval(175, 175, 225, 225, fill="red")

    def move(event):
        canva.coords(ball, event.x - 25, event.y - 25, event.x + 25, event.y + 25)

    canva.bind("<Motion>", move)
    window.mainloop()


def lesson_4_owl_home():
    from tkinter import messagebox

    def move(event):
        key = event.keysym
        home_coord = canva.coords(home)
        sova_coord = canva.coords(sova)
        if sova_coord[0] >= home_coord[0] + 50 and 150 <= sova_coord[1] + 50 <= 170:
            messagebox.showinfo("готово", "Сова дома!")
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
    window.title("Верни сову домой - Урок 4")

    canva = Canvas(window, width=600, height=600, bg="lightblue")
    canva.pack()

    image_path = os.path.join(os.path.dirname(__file__), "images", "test.png")
    image = PhotoImage(file=image_path)
    sova = canva.create_image(300, 300, image=image)
    home = canva.create_rectangle(400, 150, 600, 200, fill="brown")

    window.bind("<KeyPress>", move)
    window.mainloop()


# ======================== УРОК 5: Промежуточный проект - Снегопад ========================

def lesson_5_snowfall():
    def move_basket(event):
        key = event.keysym
        if key == "Left":
            canva.move(basket, -10, 0)
        elif key == "Right":
            canva.move(basket, 10, 0)

    def increase_score():
        global score
        score += 1
        score_label.config(text=f"Счет: {score}")

    def check_collision():
        basket_coords = canva.coords(basket)
        for snowflake in snowflakes[:]:
            snowflake_coords = canva.coords(snowflake)
            if snowflake_coords:
                if (basket_coords[0] - 75 < snowflake_coords[0] < basket_coords[0] + 75 and
                        basket_coords[1] - 25 < snowflake_coords[1] < basket_coords[1] + 25):
                    increase_score()
                    canva.delete(snowflake)
                    snowflakes.remove(snowflake)

    def move_snowflake(snowflake):
        coords = canva.coords(snowflake)
        if coords:
            x, y = coords
            canva.move(snowflake, 0, snowflake_speed)
            if y < 600:
                canva.after(50, move_snowflake, snowflake)
            else:
                canva.delete(snowflake)
                if snowflake in snowflakes:
                    snowflakes.remove(snowflake)
                create_snowflake()

    def create_snowflake():
        x = random.randint(0, 600)
        y = 0
        snowflake = canva.create_image(x, y, image=image)
        snowflakes.append(snowflake)
        move_snowflake(snowflake)

    def spawn_snowflake():
        create_snowflake()
        canva.after(2000, spawn_snowflake)
        check_collision()

    global score, snowflake_speed, snowflakes

    window = Tk()
    window.geometry("600x650")
    window.title("СНЕГОПАД")
    window.resizable(False, False)

    canva = Canvas(window, width=600, height=600, bg="lightblue")
    canva.pack()

    image_path = os.path.join(os.path.dirname(__file__), "images", "snow.png")
    image = PhotoImage(file=image_path)

    basket_path = os.path.join(os.path.dirname(__file__), "images", "basket.png")
    basket_image = PhotoImage(file=basket_path)
    basket = canva.create_image(400, 500, image=basket_image)

    snowflake_speed = 5
    snowflakes = []
    score = 0

    score_label = Label(window, text=f"Счет: {score}", font=("Arial", 16))
    score_label.pack()

    spawn_snowflake()

    window.bind("<KeyPress>", move_basket)
    window.mainloop()


# =====================================================================
# УРОКИ 6-18: СИМУЛЯТОР АВТОСЕРВИСА (simulator_avtoservis)
# =====================================================================

# --- Урок 6: Создание базы данных и окна ---

class ConnectDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def select_sql(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_sql(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


class MyWindow:
    def __init__(self):
        self.kol_avto = 0
        self.servis_finish = False
        self.servis1_crossed = False
        self.servis2_crossed = False
        self.servis3_crossed = False
        self.servis4_crossed = False
        self.start_time = None
        self.window = None
        self.canva = None
        self.current_id_user = None
        self.admin = False
        self.car_image = None
        self.work_window = None
        self.table_lider = None

        self.create_start_window()

    def visible_window(self):
        if self.window:
            self.window.mainloop()

    def destroy_main_window(self):
        if self.window:
            self.window.destroy()

    # --- Урок 7: Виджеты (Label, Entry, Button) ---

    def widget_for_start_window(self):
        self.label_login = MyLabel(self.window, "Логин", 100, 50)
        self.label_password = MyLabel(self.window, "Пароль", 100, 100)

        self.entry_login = MyEntry(self.window, 200, 50, False)
        self.entry_password = MyEntry(self.window, 200, 100, True)

        self.show_btn = MyButton(self.window, 200, 150, "Показать пароль", "show", self)
        self.enter_btn = MyButton(self.window, 200, 200, "Войти", "enter", self)

        self.lider_btn = MyButton(self.window, 200, 250, "Список лидеров", "lider", self)

        # --- Урок 16: Меню ---
        self.main_menu = Menu(self.window, tearoff=0)
        self.file_menu = Menu(self.window, tearoff=0)
        self.file_menu.add_command(label="О программе", command=self.about)
        self.file_menu.add_command(label="Выход", command=self.exit_app)
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.window.config(menu=self.main_menu)

        # --- Урок 13: Таблица лидеров ---
        self.create_table_lider()

    # --- Урок 7: Классы для виджетов ---

    def widget_for_work_window(self):
        title = MyLabel(self.work_window, "Список работ", 100, 10)
        self.step1 = MyCheckButton(self.work_window, "Доставить машину в мастерскую", 50, 80)
        self.step2 = MyCheckButton(self.work_window, "Сделать полный осмотр", 50, 110)
        self.step3 = MyCheckButton(self.work_window, "Помыть машину", 50, 140)
        self.step4 = MyCheckButton(self.work_window, "Провести ремонт", 50, 170)
        self.step5 = MyCheckButton(self.work_window, "Установить сигнализацию", 50, 200)
        self.step6 = MyCheckButton(self.work_window, "Поставить машину обратно в гараж", 50, 230)

        info_text = self.canva.create_text(400, 50, text="НАЖМИТЕ ДЛЯ НАЧАЛА РАБОТЫ",
                                            font=("Arial", 16), fill="blue", activefill="red", tags="start_work")
        self.canva.tag_bind("start_work", "<Button-1>", lambda e: self.start_work(e))

        # --- Урок 14: Кнопка назад ---
        back_btn = MyButton(self.work_window, 400, 600, "Назад", "back", self)

    # --- Урок 7: Canvas creation ---

    def canva_for_work_window(self):
        self.canva = Canvas(self.work_window, width=800, height=800, bg="lightgray")
        self.canva.pack()

        self.canva.create_rectangle(50, 400, 300, 600, width=3, outline="black")
        self.canva.create_text(175, 420, text="МАСТЕРСКАЯ", font=("Arial", 14))

        self.canva.create_rectangle(550, 400, 750, 600, width=3, outline="black")
        self.canva.create_text(650, 420, text="ГАРАЖ", font=("Arial", 14))

        # --- Урок 12: Таймер ---
        self.txt_timer = self.canva.create_text(700, 50, text="0 сек", font=("Arial", 20), fill="black")

        # --- Урок 9: Счетчик машин ---
        self.txt_kol_avto = self.canva.create_text(
            400, 700, text="Обслужено машин: " + str(self.kol_avto), font=("Arial", 16), fill="black"
        )

    # --- Урок 1: Timer method ---

    def update_timer(self):
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.canva.itemconfig(self.txt_timer, text=f"{elapsed} сек")
            self.canva.after(1000, self.update_timer)

    # --- Урок 10: Start work ---

    def start_work(self, event):
        self.canva.delete("start_work")

        car_list = [
            os.path.join(os.path.dirname(__file__), "images", "car1.png"),
            os.path.join(os.path.dirname(__file__), "images", "car2.png"),
            os.path.join(os.path.dirname(__file__), "images", "car3.png"),
            os.path.join(os.path.dirname(__file__), "images", "car4.png"),
            os.path.join(os.path.dirname(__file__), "images", "car5.png"),
            os.path.join(os.path.dirname(__file__), "images", "car6.png"),
            os.path.join(os.path.dirname(__file__), "images", "car7.png"),
            os.path.join(os.path.dirname(__file__), "images", "car8.png"),
        ]

        self.random_car_file = random.choice(car_list)
        self.car_image = PhotoImage(file=self.random_car_file)

        s1_path = os.path.join(os.path.dirname(__file__), "images", "s1.png")
        s2_path = os.path.join(os.path.dirname(__file__), "images", "s2.png")
        s3_path = os.path.join(os.path.dirname(__file__), "images", "s3.png")
        s4_path = os.path.join(os.path.dirname(__file__), "images", "s4.png")

        self.servis_images = [
            PhotoImage(file=s1_path),
            PhotoImage(file=s2_path),
            PhotoImage(file=s3_path),
            PhotoImage(file=s4_path),
        ]

        self.car = self.canva.create_image(650, 500, image=self.car_image)

        # --- Урок 12: Timer start ---
        self.start_time = time.time()
        self.update_timer()

        self.canva.focus_set()
        self.canva.bind("<KeyPress>", self.move_car)

    # --- Урок 10: Move car ---

    def move_car(self, event):
        key = event.keysym
        coords = self.canva.coords(self.car)

        if key == "Left":
            if coords[0] > 30:
                self.canva.move(self.car, -10, 0)
        elif key == "Right":
            if coords[0] < 770:
                self.canva.move(self.car, 10, 0)
        elif key == "Up":
            if coords[1] > 30:
                self.canva.move(self.car, 0, -10)
        elif key == "Down":
            if coords[1] < 770:
                self.canva.move(self.car, 0, 10)

        coords = self.canva.coords(self.car)
        # Check if car is in workshop
        if 50 < coords[0] < 200 and 400 < coords[1] < 600 and not self.servis_finish:
            messagebox.showinfo("info", "Машина в мастерской! Начните обслуживание!")
            self.canva.unbind("<KeyPress>")
            self.create_servis()
            self.step1.set_state()

        # Check if car is back in garage
        if 650 < coords[0] < 750 and 400 < coords[1] < 600 and self.servis_finish:
            self.step6.set_state()
            messagebox.showinfo("info", "Машина в гараже! Работа завершена!")
            self.kol_avto += 1
            self.canva.itemconfig(self.txt_kol_avto, text="Обслужено машин: " + str(self.kol_avto))

            # --- Урок 12: Save to DB ---
            try:
                db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
                elapsed = int(time.time() - self.start_time)
                db.insert_sql(
                    f"INSERT INTO work_user (id_user, count_avto, sec) VALUES ({self.current_id_user}, {self.kol_avto}, {elapsed})"
                )
                db.close()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка записи в БД: {e}")

            # --- Урок 11: Ask continue ---
            otvet = messagebox.askyesno("Продолжить?", "Желаете продолжить работу?")
            if otvet:
                self.reset_game()
            else:
                messagebox.showinfo("Конец дня", f"Рабочий день завершен! Обслужено машин: {self.kol_avto}")
                if self.work_window:
                    self.work_window.destroy()

    # --- Урок 10: Create services ---

    def create_servis(self):
        positions = [(100, 650), (220, 650), (100, 350), (220, 350)]
        for i, (x, y) in enumerate(positions):
            servis = self.canva.create_image(x, y, image=self.servis_images[i], tags=f"servis{i+1}")
            self.canva.tag_bind(f"servis{i+1}", "<Button-1>", lambda e, n=i + 1: self.cross_servis(n))

    # --- Урок 11: Cross service ---

    def cross_servis(self, num):
        if num == 1 and not self.servis1_crossed:
            messagebox.showinfo("info", "Услуга 1 проведена!")
            self.canva.create_line(75, 625, 125, 675, width=3, fill="red", tags="cross1")
            self.servis1_crossed = True
            self.step2.set_state()

        elif num == 2 and not self.servis2_crossed:
            messagebox.showinfo("info", "Услуга 2 проведена!")
            self.canva.create_line(195, 625, 245, 675, width=3, fill="red", tags="cross2")
            self.servis2_crossed = True
            self.step3.set_state()

        elif num == 3 and not self.servis3_crossed:
            messagebox.showinfo("info", "Услуга 3 проведена!")
            self.canva.create_line(75, 325, 125, 375, width=3, fill="red", tags="cross3")
            self.servis3_crossed = True
            self.step4.set_state()

        elif num == 4 and not self.servis4_crossed:
            messagebox.showinfo("info", "Услуга 4 проведена!")
            self.canva.create_line(195, 325, 245, 375, width=3, fill="red", tags="cross4")
            self.servis4_crossed = True
            self.step5.set_state()

        if self.servis1_crossed and self.servis2_crossed and self.servis3_crossed and self.servis4_crossed:
            self.servis_finish = True
            self.canva.focus_set()
            self.canva.bind("<KeyPress>", self.move_car)

    # --- Урок 11: Reset game ---

    def reset_game(self):
        self.servis_finish = False
        self.servis1_crossed = False
        self.servis2_crossed = False
        self.servis3_crossed = False
        self.servis4_crossed = False

        self.canva.delete("car")
        self.canva.delete("cross1", "cross2", "cross3", "cross4")
        self.canva.delete("servis1", "servis2", "servis3", "servis4")

        self.step1.reset()
        self.step2.reset()
        self.step3.reset()
        self.step4.reset()
        self.step5.reset()
        self.step6.reset()

        self.start_time = time.time()

        car_list = [
            os.path.join(os.path.dirname(__file__), "images", "car1.png"),
            os.path.join(os.path.dirname(__file__), "images", "car2.png"),
            os.path.join(os.path.dirname(__file__), "images", "car3.png"),
            os.path.join(os.path.dirname(__file__), "images", "car4.png"),
            os.path.join(os.path.dirname(__file__), "images", "car5.png"),
            os.path.join(os.path.dirname(__file__), "images", "car6.png"),
            os.path.join(os.path.dirname(__file__), "images", "car7.png"),
            os.path.join(os.path.dirname(__file__), "images", "car8.png"),
        ]
        self.random_car_file = random.choice(car_list)
        self.car_image = PhotoImage(file=self.random_car_file)
        self.car = self.canva.create_image(650, 500, image=self.car_image, tags="car")
        self.canva.focus_set()
        self.canva.bind("<KeyPress>", self.move_car)

    # --- Урок 13: Table lider ---

    def create_table_lider(self):
        self.table_lider = ttk.Treeview(self.window, columns=("user", "min"), show="headings", height=8)
        self.table_lider.heading("user", text="Пользователь")
        self.table_lider.heading("min", text="Рекорд (сек)")
        self.table_lider.column("user", width=150, anchor="center")
        self.table_lider.column("min", width=150, anchor="center")

    def show_table_lider(self):
        # Clear existing data
        for item in self.table_lider.get_children():
            self.table_lider.delete(item)

        # Load data from DB
        try:
            db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
            result = db.select_sql("""
                SELECT users.login, MIN(work_user.sec) as min_sec
                FROM users
                JOIN work_user ON users.id = work_user.id_user
                GROUP BY users.login
                ORDER BY min_sec ASC
            """)
            db.close()
            for row in result:
                self.table_lider.insert("", "end", values=(row[0], row[1]))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки данных: {e}")

        self.table_lider.pack()

    def delete_table_lider(self):
        self.table_lider.pack_forget()

    # --- Урок 14: Admin panel ---

    def widget_for_admin_window(self):
        title = MyLabel(self.admin_window, "Панель управления", 130, 20)

        add_btn = MyButton(self.admin_window, 150, 80, "Добавить пользователя", "new_user", self)
        del_btn = MyButton(self.admin_window, 150, 130, "Удалить пользователя", "del_user", self)
        upd_btn = MyButton(self.admin_window, 150, 180, "Изменить пароль", "update_user", self)
        back_btn = MyButton(self.admin_window, 150, 250, "Назад", "back", self)

    # --- Урок 16: Menu methods ---

    def about(self):
        about_file = os.path.join(os.path.dirname(__file__), "about.txt")
        subprocess.run(["notepad", about_file])

    def exit_app(self):
        sys.exit(0)

    # --- Helper: create start window ---

    def create_start_window(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.title("ВХОД")
        self.widget_for_start_window()


# --- Урок 7: MyLabel class ---

class MyLabel:
    def __init__(self, window, text, x, y):
        self.label = Label(window, text=text, font=("Arial", 14), bg="lightgray")
        self.label.place(x=x, y=y)


# --- Урок 7: MyEntry class ---

class MyEntry:
    def __init__(self, window, x, y, hidden):
        if hidden:
            self.entry = Entry(window, show="*")
        else:
            self.entry = Entry(window)
        self.entry.place(x=x, y=y)


# --- Урок 7, 8, 14, 15: MyButton class ---

class MyButton:
    def __init__(self, window, x, y, text, command, my_window):
        self.window = window
        self.my_window = my_window
        self.btn = Button(window, text=text, font=("Arial", 12), command=lambda: self.click(command, my_window))
        self.btn.place(x=x, y=y)

    def click(self, command, my_window):
        if command == "enter":
            self.enter()
        elif command == "show":
            self.show()
        elif command == "lider":
            self.lider_table()
        elif command == "new_user":
            self.new_user()
        elif command == "del_user":
            self.del_user()
        elif command == "update_user":
            self.update_user()
        elif command == "back":
            self.back()

    # --- Урок 8: Enter method ---

    def enter(self):
        self.my_window.admin = False
        login = self.my_window.entry_login.entry.get()
        password = self.my_window.entry_password.entry.get()

        try:
            db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
            sql = db.select_sql("SELECT * FROM users")
            db.close()
        except Exception as e:
            messagebox.showerror("Ошибка БД", f"Не удалось подключиться к БД: {e}")
            return

        open_access = False
        for row in sql:
            if row[1] == login and row[2] == password:
                open_access = True
                global id_user
                id_user = row[0]
                self.my_window.current_id_user = row[0]
                if login == "admin":
                    self.my_window.admin = True
                break

        if open_access:
            messagebox.showinfo("Доступ", "Доступ разрешен!")

            if self.my_window.admin:
                self.my_window.destroy_main_window()
                self.my_window.admin_window = Tk()
                self.my_window.admin_window.geometry("400x300")
                self.my_window.admin_window.title("Панель управления")
                self.my_window.widget_for_admin_window()
                self.my_window.admin_window.mainloop()
            else:
                self.my_window.destroy_main_window()
                self.my_window.work_window = Tk()
                self.my_window.work_window.geometry("800x800")
                self.my_window.work_window.title("Автосервис")
                self.my_window.canva_for_work_window()
                self.my_window.widget_for_work_window()
                self.my_window.work_window.mainloop()

        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")

    # --- Урок 7: Show password ---

    def show(self):
        entry = self.my_window.entry_password.entry
        if entry.cget("show") == "*":
            entry.config(show="")
        else:
            entry.config(show="*")

    # --- Урок 13: Lider table ---

    def lider_table(self):
        if not hasattr(self, 'visible'):
            self.visible = False
        if not self.visible:
            self.my_window.show_table_lider()
            self.visible = True
        else:
            self.my_window.delete_table_lider()
            self.visible = False

    # --- Урок 15: New user ---

    def new_user(self):
        user_login = simpledialog.askstring("Новый пользователь", "Введите логин:")
        user_password = simpledialog.askstring("Новый пользователь", "Введите пароль:")
        if user_login and user_password:
            try:
                db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
                db.insert_sql(f"INSERT INTO users (login, password) VALUES ('{user_login}', '{user_password}')")
                db.close()
                messagebox.showinfo("Успех", "Пользователь добавлен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {e}")

    # --- Урок 15: Delete user ---

    def del_user(self):
        user_login = simpledialog.askstring("Удаление", "Введите логин пользователя:")
        if user_login:
            confirm = messagebox.askyesno("Подтверждение", f"Удалить пользователя {user_login}?")
            if confirm:
                try:
                    db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
                    db.insert_sql(f"DELETE FROM users WHERE login = '{user_login}'")
                    db.close()
                    messagebox.showinfo("Успех", "Пользователь удален!")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка: {e}")

    # --- Урок 15: Update password ---

    def update_user(self):
        user_login = simpledialog.askstring("Обновление", "Введите логин пользователя:")
        user_password = simpledialog.askstring("Обновление", "Введите новый пароль:")
        if user_login and user_password:
            confirm = messagebox.askyesno("Подтверждение", f"Изменить пароль {user_login}?")
            if confirm:
                try:
                    db = ConnectDB(os.path.join(os.path.dirname(__file__), "avtoservis_users.db"))
                    db.insert_sql(f"UPDATE users SET password = '{user_password}' WHERE login = '{user_login}'")
                    db.close()
                    messagebox.showinfo("Успех", "Пароль изменен!")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка: {e}")

    # --- Урок 15: Back button ---

    def back(self):
        if hasattr(self.my_window, 'work_window') and self.my_window.work_window:
            self.my_window.work_window.destroy()
        if hasattr(self.my_window, 'admin_window') and self.my_window.admin_window:
            self.my_window.admin_window.destroy()
        self.my_window.create_start_window()
        self.my_window.visible_window()


# --- Урок 9: MyCheckButton class ---

class MyCheckButton:
    def __init__(self, window, text, x, y):
        self.var = BooleanVar()
        self.cb = Checkbutton(window, text=text, font=("Arial", 12), variable=self.var,
                              state="disabled", disabledforeground="black")
        self.cb.place(x=x, y=y)

    def set_state(self):
        self.cb.config(state="normal")
        self.var.set(True)
        self.cb.config(state="disabled", disabledforeground="green")

    def reset(self):
        self.cb.config(state="normal")
        self.var.set(False)
        self.cb.config(state="disabled", disabledforeground="black")


# ======================== ФУНКЦИЯ ЗАПУСКА ========================

def main():
    print("=== Модуль 3: Все уроки ===")
    print("Выберите урок для запуска:")
    print("1 - Праздничная гирлянда")
    print("2 - Гонка шаров")
    print("3 - Прыгающие шары")
    print("4 - Управление мышкой")
    print("5 - Верни сову домой")
    print("6 - Снегопад")
    print("7 - Симулятор автосервиса (уроки 6-18)")
    print()
    choice = input("Введите номер урока (1-7): ").strip()

    if choice == "1":
        lesson_1_garland()
    elif choice == "2":
        lesson_2_ball_race()
    elif choice == "3":
        lesson_3_bouncing_balls()
    elif choice == "4":
        lesson_4_mouse_control()
    elif choice == "5":
        lesson_4_owl_home()
    elif choice == "6":
        lesson_5_snowfall()
    elif choice == "7":
        app = MyWindow()
        app.visible_window()
    else:
        print("Неверный выбор!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        lesson_map = {
            "1": lesson_1_garland,
            "2": lesson_2_ball_race,
            "3": lesson_3_bouncing_balls,
            "4": lesson_4_mouse_control,
            "5": lesson_4_owl_home,
            "6": lesson_5_snowfall,
            "7": lambda: MyWindow().visible_window(),
        }
        lesson = sys.argv[1]
        if lesson in lesson_map:
            lesson_map[lesson]()
        else:
            main()
    else:
        main()
