class Page:
    def __init__(self, window):
        self.elements = []
        self.window = window

    def register_ui(self, element):
        self.elements.append(element)
        return element

    def destroy_main_window(self):
        for element in self.elements:
            element.destroy()
        self.elements.clear()

    def exit(self):
        self.destroy_main_window()