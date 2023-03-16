import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLP Aproximação")
        # self.geometry("900x600")

        self.create_widgets()
        self.create_plots()

    def create_widgets(self):
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

        self.function_label = ttk.Label(self.input_frame, text="Função: f(x) = sen(x/2) ∙ cos(2x)", font=("Helvetica", 13))
        self.function_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.min_x_label = ttk.Label(self.input_frame, text="x mínimo:", font=("Helvetica", 13))
        self.min_x_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.min_x_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.min_x_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.max_x_label = ttk.Label(self.input_frame, text="x máximo:", font=("Helvetica", 13))
        self.max_x_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.max_x_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.max_x_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.learning_rate_label = ttk.Label(self.input_frame, text="Taxa de aprendizagem:", font=("Helvetica", 13))
        self.learning_rate_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.learning_rate_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.learning_rate_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.neurons_label = ttk.Label(self.input_frame, text="Quantidade de neurônios:", font=("Helvetica", 13))
        self.neurons_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.neurons_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.neurons_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.samples_label = ttk.Label(self.input_frame, text="Quantidade de amostras:", font=("Helvetica", 13))
        self.samples_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.samples_entry = ttk.Entry(self.input_frame, font=("Helvetica", 13))
        self.samples_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.error_value_label = ttk.Label(self.input_frame, text="Valor do erro atual:", font=("Helvetica", 13))
        self.error_value_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.error_value = ttk.Label(self.input_frame, text="0.000", font=("Helvetica", 13))
        self.error_value.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.cycles_label = ttk.Label(self.input_frame, text="Número de ciclos:", font=("Helvetica", 13))
        self.cycles_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.cycles_value = ttk.Label(self.input_frame, text="0", font=("Helvetica", 13))
        self.cycles_value.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        self.approximate_button = tk.Button(self.input_frame, text="Aproximar", font=("Helvetica", 13))
        self.approximate_button.grid(row=8, column=0, columnspan=2, pady=5)


    def create_plots(self):
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        y3 = np.tan(x)

        self.plot_frame = ttk.Frame(self)
        self.plot_frame.pack(side=tk.TOP, pady=10)

        self.fig1, ax1 = plt.subplots(figsize=(4, 3))
        ax1.plot(x, y1)
        ax1.set_title("Verdadeiro")
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.input_frame)
        self.canvas1.get_tk_widget().grid(row=0, column=2, rowspan=9, padx=(5, 0), pady=5, sticky='E')

        self.fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.plot(x, y2)
        ax2.set_title("Aproximação MLP")
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.plot_frame)
        self.canvas2.get_tk_widget().grid(row=0, column=0, padx=(0, 5), pady=5, sticky='W')

        self.fig3, ax3 = plt.subplots(figsize=(4, 3))
        ax3.plot(x, y3)
        ax3.set_title("Erro por ciclo")
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.plot_frame)
        self.canvas3.get_tk_widget().grid(row=0, column=1, padx=(5, 0), pady=5, sticky='E')

if __name__ == "__main__":
    app = App()
    app.mainloop()

