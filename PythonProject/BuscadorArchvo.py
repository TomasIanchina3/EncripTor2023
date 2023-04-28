
import os
import  tkinter as tk
from tkinter  import filedialog

ventana = tk.Tk()

ruta_archivo = filedialog.askopenfilename()

print(ruta_archivo)
with open(ruta_archivo) as ar_object:
    texto = ar_object.read()
    print(texto)