from os import open
from tkinter import filedialog


def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename()
    try:
        with open(path=ruta_archivo, mode="rt") as file:
            print(file.read())
    except FileNotFoundError:
        print("ERROR! Archivo no encotrado.")
        seleccionar_archivo()