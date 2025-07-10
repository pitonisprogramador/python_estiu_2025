import tkinter as tk
from tkinter import filedialog as fd
import io
import re
import time

def funcio():
    cadena = e1.get()
    lista = cadena.split(',')
    resultado = []

    for numero in lista:
        resultado.append(int(numero))

    # resultado = [int(numero) for numero in lista] # LIST COMPREHENSION
    # resultado = [1, 2, 3, 4, 5]

    suma = 0
    for numero in resultado:
        suma += numero ** 3

    Label1.config(text=f"{suma}")

root = tk.Tk()
amplada = root.winfo_screenwidth()//2
alçada = root.winfo_screenheight()//2
root.geometry(f"{amplada}x{alçada}")

cl = tk.Canvas(root, bg="#FFD700", width=amplada, height=alçada)
cl.place(x=0, y=0)

b1=tk.Button(cl, text="Press for result", command=funcio)
b1.place(x = amplada // 2, y = 8 * alçada // 10, width=100, height=25, anchor = tk.CENTER)

e1=tk.Entry(cl, text="Calcularemos suma de cubos de elementos separados por coma")
e1.place(x = amplada // 2, y = 4 * alçada // 10, width=100, height=25, anchor = tk.CENTER)

Label1 = tk.Label(cl, text = "SUMA DE CUBOS", width=0, font = ('Arial', 10), bg = cl.cget('bg'))
Label1.place(x = amplada // 2, y = 6 * alçada // 10, anchor = "center")

root.mainloop()