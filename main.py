import tkinter as tk
from tkinter import Entry, StringVar, ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.perceptron.multilayer_perceptron import MultilayerPerceptron


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLP Aproximação")
        self.resizable(False, False)

        self.create_widgets()
        self.create_plots()

    def aproximar(self, _=None):
        mlp = MultilayerPerceptron(int(self.neurons_entry.get()), float(self.learning_rate_entry.get()), float(self.max_x_entry.get()), float(
            self.min_x_entry.get()), int(self.samples_entry.get()), float(self.tolerated_error_entry.get()), self.var_erro, self.var_ciclo, self)

        mlp.initialize((self.canvas1, self.ax1), (self.canvas2,
                       self.ax2), (self.canvas3, self.ax3))

    def create_widgets(self):
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

        self.function_label = ttk.Label(
            self.input_frame, text="Função: f(x) = sen(x/2) ∙ cos(2x)", font=("Helvetica", 13))
        self.function_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.min_x_label = ttk.Label(
            self.input_frame, text="x mínimo:", font=("Helvetica", 13))
        self.min_x_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.min_x_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.min_x_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.max_x_label = ttk.Label(
            self.input_frame, text="x máximo:", font=("Helvetica", 13))
        self.max_x_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.max_x_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.max_x_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.tolerated_error_label = ttk.Label(
            self.input_frame, text="Erro Tolerado:", font=("Helvetica", 13))
        self.tolerated_error_label.grid(
            row=3, column=0, padx=5, pady=5, sticky="w")

        self.tolerated_error_entry = ttk.Entry(
            self.input_frame, font=("Helvetica", 13))
        self.tolerated_error_entry.grid(
            row=3, column=1, padx=5, pady=5, sticky="w")

        self.learning_rate_label = ttk.Label(
            self.input_frame, text="Taxa de aprendizagem:", font=("Helvetica", 13))
        self.learning_rate_label.grid(
            row=4, column=0, padx=5, pady=5, sticky="w")

        self.learning_rate_entry = ttk.Entry(
            self.input_frame, font=("Helvetica", 13))
        self.learning_rate_entry.grid(
            row=4, column=1, padx=5, pady=5, sticky="w")

        self.neurons_label = ttk.Label(
            self.input_frame, text="Quantidade de neurônios:", font=("Helvetica", 13))
        self.neurons_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.neurons_entry = ttk.Entry(
            self.input_frame, font=("Helvetica", 13))
        self.neurons_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.samples_label = ttk.Label(
            self.input_frame, text="Quantidade de amostras:", font=("Helvetica", 13))
        self.samples_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.samples_entry = ttk.Entry(
            self.input_frame, font=("Helvetica", 13))
        self.samples_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.error_value_label = ttk.Label(
            self.input_frame, text="Valor do erro atual:", font=("Helvetica", 13))
        self.error_value_label.grid(
            row=7, column=0, padx=5, pady=5, sticky="w")

        self.var_erro = StringVar()
        self.var_erro.set("0.000000")

        self.error_value = ttk.Label(
            self.input_frame, textvariable=self.var_erro, font=("Helvetica", 13))
        self.error_value.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        self.cycles_label = ttk.Label(
            self.input_frame, text="Número de ciclos:", font=("Helvetica", 13))
        self.cycles_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        self.var_ciclo = StringVar()
        self.var_ciclo.set(0)

        self.cycles_value = ttk.Label(
            self.input_frame, textvariable=self.var_ciclo, font=("Helvetica", 13))
        self.cycles_value.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        self.approximate_button = tk.Button(self.input_frame, text="Aproximar", font=(
            "Helvetica", 13), command=self.aproximar)
        self.approximate_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.approximate_button.bind('<Return>', self.aproximar)

        self.debug()

    def debug(self):
        self.min_x_entry.insert(0, '-1')
        self.max_x_entry.insert(0, '1')
        self.tolerated_error_entry.insert(0, '0.05')
        self.learning_rate_entry.insert(0, '0.005')
        self.neurons_entry.insert(0, '200')
        self.samples_entry.insert(0, '50')

    def create_plots(self):
        start = []

        self.plot_frame = ttk.Frame(self)
        self.plot_frame.pack(side=tk.TOP, pady=15)

        self.fig1, self.ax1 = plt.subplots(figsize=(4, 3))
        self.ax1.plot(start, start)
        self.ax1.set_title("Função Aproximada")
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.input_frame)
        self.canvas1.get_tk_widget().grid(row=0, column=2, rowspan=10,
                                          padx=(5, 0), pady=5, sticky='E')

        self.fig2, self.ax2 = plt.subplots(figsize=(4, 3))
        self.ax2.plot(start, start)
        self.ax2.set_title("Aproximação MLP x Real")
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.plot_frame)
        self.canvas2.get_tk_widget().grid(row=0, column=0, padx=(0, 5), pady=5, sticky='W')

        self.fig3, self.ax3 = plt.subplots(figsize=(4, 3))
        self.ax3.plot(start, start)
        self.ax3.set_title("Erro por ciclo")
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.plot_frame)
        self.canvas3.get_tk_widget().grid(row=0, column=1, padx=(5, 0), pady=5, sticky='E')


if __name__ == "__main__":
    app = App()
    app.mainloop()
