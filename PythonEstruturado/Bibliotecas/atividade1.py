#Utilizando o PyCharm, crie um programa com interface gráfica em Python que receba dois números,
# compare-os e informe se o primeiro é maior, menor ou igual ao segundo.

import tkinter as tk
from pydoc import text
from tkinter import messagebox

def compara_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if num1 > num2:
        resultado = f"O primeiro número {num1} é maior que segundo {num2}"
    if num1 < num2:
        resultado = f"O primeiro número {num2} é menor que o segundo {num1}"
    if num1 == num2:
        resultado = "Os dois números são iguais"

    messagebox.showinfo("Resultado", resultado)

#Criando a janela
janela = tk.Tk()
janela.title("Comparando números")

#Criando os widgets
label_num1 = tk.Label(janela, text="Número 1: ")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_compara = tk.Button(janela, text="Comparar", command=compara_numeros)
botao_compara.grid(row=2, column=0, padx=10, pady=5)

#Roda o loop
janela.mainloop()