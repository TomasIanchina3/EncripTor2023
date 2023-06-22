#!/usr/bin/env python3

import tkinter
import random
import customtkinter
from tkinter import filedialog



def encriptar(llave):
        # Primero vamos a generar el número aleatorio entre 1 y 4
        encriptado = bytearray()
        key_length = len(llave)

        ruta_archivo = filedialog.askopenfilename()

        print(ruta_archivo)
        with open(ruta_archivo) as ar_object:
            texto = ar_object.read()

        # Una vez leído el archivo en la cadena
        # Lo remplazamos con el encriptado utilizando un bucle que recorrerá esa cadena
        for i, char in enumerate(texto):
            # Generamos un valor de clave aleatorio en cada iteración
            random.seed(int(llave[i % key_length]))
            # Ahora procederemos a aplicar la operación XOR
            encriptado.append(ord(char) ^ random.randint(0, 255))

        with open(ruta_archivo, 'wb') as ar_object:  # Utilizamos 'ab' para modo de escritura en modo binario
            ar_object.write(encriptado)


def desencriptar(llave):
    ruta_archivo = filedialog.askopenfilename()
    desencriptado = bytearray()
    key_length = len(llave)

    with open(ruta_archivo, 'rb') as ar_object:  # Utilizamos 'rb' para modo de lectura en modo binario
        texto = ar_object.read()

    # Aquí vamos a hacer el proceso inverso al que aplicamos en encriptado
    for i, char in enumerate(texto):
        random.seed(int(llave[i % key_length]))
        desencriptado.append(char ^ random.randint(0, 255))

    with open(ruta_archivo, 'wb') as ar_object:  # Utilizamos 'wb' para modo de escritura en modo binario
        ar_object.write(desencriptado)

#Crear Llave
llave = bytearray([random.randint(0,255) for _ in range(32)])
# Creacion ventana
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Grupo K_Metodología de la Investigación")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="EncripTor 2023")
label.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Encriptar", width=200, height=50,
                                  command=lambda: encriptar(llave))
button1.pack(pady=20, padx=10)
button1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=frame, text="Desencriptar", width=200, height=50,
                                  command=lambda: desencriptar(llave))
button2.pack(pady=20, padx=10)
button2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()


