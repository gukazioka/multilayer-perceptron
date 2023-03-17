def CentralizeWindow(self):
    width = self.winfo_reqwidth()
    height = self.winfo_reqheight()
    x = (self.winfo_screenwidth() // 3) - (width)
    y = (self.winfo_screenheight() // 4) - (height)
    self.geometry(f"+{x}+{y}")

def CentralizeNotify(self):
    width = self.winfo_reqwidth()
    height = self.winfo_reqheight()
    x = (self.winfo_screenwidth() // 2) - (width)
    y = (self.winfo_screenheight() // 2) - (height)
    self.geometry(f"+{x}+{y}")