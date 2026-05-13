from module3_main.simulator_autoservis.ui.base_label import BaseLabel
from module3_main.simulator_autoservis.ui.base_button import BaseButton
from module3_main.simulator_autoservis.window_manager import WindowManager
from module3_main.simulator_autoservis.ui.base_entry import BaseEntry
from .page import Page
from tkinter import messagebox
from module3_main.simulator_autoservis.repository import Repository

class LoginPage(Page):
    def __init__(self, window):
        super().__init__(window)

    def enter(self):
        self.widget_for_start_window()

    def widget_for_start_window(self):
        self.label_title = super().register_ui(BaseLabel('vxod', "Arial 20 bold", "Lightblue", 150, 50))
        self.label_login = super().register_ui(BaseLabel("login", "Arial 15", "Lightblue", 50, 150))
        self.label_password = super().register_ui(BaseLabel('Password', "Arial 15", "Lightblue", 50, 200))
        self.entry_login = super().register_ui(BaseEntry("Arial 15", 150, 150, 150, False))
        self.entry_password = super().register_ui(BaseEntry("Arial 15", 150, 200, 150, True))

        self.entry_password_entry = self.entry_password.entry

        self.enter_btn = super().register_ui(BaseButton("ВХОД", "Arial 15", 150, 300, 100, self.onSumbut))
        self.show_btn = super().register_ui(BaseButton("⁐", "Arial 12", 310, 200, 35, self.onShowHint))

    def on_enter(self):
        WindowManager.singletone().change_window()

    def onShowHint(self):
        if self.entry_password_entry.cget('show') == '':
            self.entry_password_entry.config(show='*')
        else:
            self.entry_password_entry.config(show='')

    def onSumbut(self):
        self.value_login = self.entry_login.value.get()
        self.value_pass = self.entry_password.value.get()

        data = Repository.singletone().get_user_by_login_password(self.value_login, self.value_pass)

        # print(data)
        #
        # if data is None:
        #     messagebox.showerror('Внимание!', 'Неверный логин и пароль')
        # else:
        #     messagebox.showinfo('Внимание!', 'Доступ разрешен')
        WindowManager.singletone().change_window('base')
