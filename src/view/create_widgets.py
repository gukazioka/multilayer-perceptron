import tkinter as tk

from tkinter import StringVar, ttk

def CreateWidget(self):
    self.input_frame = ttk.Frame(self.frame_root)
    self.input_frame.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

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