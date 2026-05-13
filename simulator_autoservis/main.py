from tkinter import *

from module3_main.simulator_autoservis.pages.base_window import BaseWindow
from module3_main.simulator_autoservis.pages.login_page import LoginPage
from repository import Repository
from window_manager import WindowManager

class Initializer:
    def __init__(self, title, size):
        self.window = Tk()
        self.mapRegister = {
            'login': LoginPage(self.window),
            'base': BaseWindow(self.window)
        }

        Repository.singletone().initialize()

        WindowManager.singletone().initialize(self.mapRegister)

        self.window.geometry(size)
        self.window.resizable(False, False)
        self.window.title(title)
        self.window.configure(bg="lightblue")

        WindowManager.singletone().change_window('login')

    def visible_window(self):
        self.window.mainloop()

    def destroy_main_mainloop(self):
        self.window.destroy()


start_window=Initializer("ВХОД", "400x400")

start_window.visible_window()

