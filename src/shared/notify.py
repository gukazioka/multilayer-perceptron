import tkinter as tk
from src.shared.centralize_window import CentralizeNotify


class Notification(tk.Toplevel):
    def __init__(self, master, message):
        super().__init__(master)
        self.title("Atenção")
        self.geometry("400x100")
        self.message = message
        self.label = tk.Label(self, text=message, padx=20, pady=20, font=("Helvetica", 13))
        self.label.pack()
        self.after(5000, self.destroy)

        CentralizeNotify(self)

