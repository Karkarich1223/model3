class WindowManager:
    instance = None

    def initialize(self, mapRegister):
        self.work_window = None
        self.current_window = None
        self.mapRegister = mapRegister

    @staticmethod
    def singletone():
        if WindowManager.instance == None:
            WindowManager.instance = WindowManager()

        return WindowManager.instance

    def change_window(self, newWindow):
        if (self.current_window):
            self.current_window.exit()

        self.current_window = self.mapRegister[newWindow]
        self.current_window.enter()