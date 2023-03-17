import tkinter as tk

class Notification(tk.Toplevel):
    def __init__(self, master, message):
        super().__init__(master)
        self.title("Notification")
        self.geometry("300x100")
        self.message = message
        self.label = tk.Label(self, text=message, padx=20, pady=20)
        self.label.pack()
        self.after(5000, self.destroy)