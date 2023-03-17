import tkinter as tk
import matplotlib.pyplot as plt

from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def CreatePlots(self):
    start = []
    self.plot_frame1 = ttk.Frame(self.frame_root)
    self.plot_frame1.pack(side=tk.RIGHT, anchor="e", padx=(90, 0))

    self.plot_frame2 = ttk.Frame(self)
    self.plot_frame2.pack(side=tk.TOP, pady=15)

    self.fig1, self.ax1 = plt.subplots(figsize=(5,4))
    self.ax1.plot(start, start)
    self.ax1.set_title("Função Aproximada")
    self.ax1.set_xlabel('x')
    self.ax1.set_ylabel('f(x)')
    self.ax1.yaxis.set_label_position('right')
    self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.plot_frame1)
    self.canvas1.get_tk_widget().grid(row=0, column=2, rowspan=10, pady=5, sticky='E')

    self.fig2, self.ax2 = plt.subplots(figsize=(5,4))
    self.ax2.plot(start, start)
    self.ax2.set_title("Aproximação MLP x Real")
    self.ax2.set_xlabel('x')
    self.ax2.set_ylabel('f(x)')
    self.ax2.yaxis.set_label_position('right')
    self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.plot_frame2)
    self.canvas2.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky='W')

    self.fig3, self.ax3 = plt.subplots(figsize=(5,4))
    self.ax3.plot(start, start)
    self.ax3.set_title("Erro por ciclo")
    self.ax3.set_xlabel('Ciclo')
    self.ax3.set_ylabel('Erro')
    self.ax3.yaxis.set_label_position('right')
    self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.plot_frame2)
    self.canvas3.get_tk_widget().grid(row=0, column=1, padx=5, pady=5, sticky='E')