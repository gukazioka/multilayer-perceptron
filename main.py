import tkinter as tk
import numpy as np

from tkinter import ttk
from src.perceptron.multilayer_perceptron import MultilayerPerceptron
from src.shared.notify import Notification
from src.shared.centralize_window import CentralizeWindow
from src.view.create_widgets import CreateWidget
from src.view.create_plots import CreatePlots


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLP Aproximação")
        self.resizable(False, False)

        self.frame_root = ttk.Frame(self)
        self.frame_root.pack(side=tk.TOP)

        CentralizeWindow(self)
        self.create_widgets()
        self.create_plots()

    def aproximar(self, _=None):
        if(self.neurons_entry.get() != '' and self.learning_rate_entry.get() != '' and
                self.max_x_entry.get() != '' and self.min_x_entry.get() != '' and
                self.samples_entry.get() != '' and self.tolerated_error_entry.get() != ''):

            mlp = MultilayerPerceptron(int(self.neurons_entry.get()), float(self.learning_rate_entry.get()), float(self.max_x_entry.get()), float(
                self.min_x_entry.get()), int(self.samples_entry.get()), float(self.tolerated_error_entry.get()), self.var_erro, self.var_ciclo, self)

            mlp.initialize(self.canvas1, self.ax1, self.canvas2,
                           self.ax2, self.canvas3, self.ax3)
        else:
            Notification(
                self, 'Erro ao aproximar! \nPor favor preencha corretamente os campos!')

    def create_widgets(self):
        CreateWidget(self)
        self.debug()

    def debug(self):
        self.min_x_entry.insert(0, '-1')
        self.max_x_entry.insert(0, '1')
        self.tolerated_error_entry.insert(0, '0.05')
        self.learning_rate_entry.insert(0, '0.005')
        self.neurons_entry.insert(0, '200')
        self.samples_entry.insert(0, '50')

    def create_plots(self):
        CreatePlots(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
