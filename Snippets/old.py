import tkinter as tk


class Svenmap(tk.Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.pack()
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        print("setting up window")
        self.window.title("svenmap")
        self.window.geometry("900x650+0+0")

    def create_widgets(self):
        print("making widgets")
        mainMenu = tk.Menu(self.window)
        self.window.config(menu=mainMenu)


mainWindow = tk.Tk()
svenMap = Svenmap(mainWindow)
svenMap.mainloop()
