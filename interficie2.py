import tkinter as tk
from tkinter import filedialog as fd
import io
import re

def estadistica(name, words):

    Label1.config(text = f"El libro ]{name} tiene {len(words)} palabras")
    

def Buscar():
    
   
    filename = fd.askopenfilename()
   
    fitxer = io.open(filename, "r", encoding = "utf-8")
    
    libro = fitxer.read()
    
    patro = re.compile("[a-zA-ZáéíóúÁÉÍÓÚ]+")
    
    palabras = patro.findall(libro)
    
    estadistica(filename, palabras)
    
    
root = tk.Tk()
amplada = root.winfo_screenwidth()//3
alcada = root.winfo_screenheight()//3
root.geometry(f"{amplada}x{alcada}")

c1 = tk.Canvas(root, bg ='#FFD700', width = amplada, height = alcada)
c1.place(x = 0, y = 0)

b1=tk.Button(c1, text = "Hazme Click",command=Buscar)
b1.place(x= amplada // 2, y= 8 * alcada//10, width=100, height=25, anchor = tk.CENTER)

Label1 = tk.Label(c1, text = "Tria l'arxiu", width = 0, font = ('Arial', 10), bg = c1.cget('bg'))
Label1.place( x = amplada//2, y = 6* alcada// 10, anchor ="center")

root.mainloop()








