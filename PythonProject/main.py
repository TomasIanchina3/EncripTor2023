#!/usr/bin/env python3

import tkinter
import random
import customtkinter
from tkinter import filedialog


def encriptar():
    # Primero vamos a generar el numero random entre 1 y 4
    llave = random.randint(1, 4)

    ruta_archivo = filedialog.askopenfilename()

    print(ruta_archivo)
    with open(ruta_archivo) as ar_object:
        texto = ar_object.read()

    # Una vez leido el archivo en la cadena
    # Lo remplazamos con el encriptado con un for que recorrera esa cadena
    encriptado = ""
    # Al ser la version beta este solo admitira el codigo ASCII pero no el codigo ASCII extendido ya que
    # deberiamos aplicar UNICODE derivando en otro metodo distinto
    for caracter in texto:
        codigoa = ord(caracter)
        if codigoa >= 32 and codigoa <= 122:
            ce = codigoa + llave
            caracterencriptado = chr(ce)
            encriptado += caracterencriptado
        else:
            encriptado += caracter

    # Ahora procederemos a modificar nuestro archivo de texto base

    with open(ruta_archivo, 'w') as ar_object:
        ar_object.write(str(llave))

    with open(ruta_archivo, 'a') as ar_object:
        ar_object.write(encriptado)
    # Para Este resultado se uso el archivo prueba para crear


def desencriptar():
    ruta_archivo = filedialog.askopenfilename()

    print(ruta_archivo)
    with open(ruta_archivo) as ar_object:
        texto = ar_object.read()
    # Aqui se repite el proceso de encriptado pero esta vez vamos a realizar las siguientes operaciones.
    # 1° Debemos identificar nuestra llave
    llave = texto[0]
    # 2° Vamos a remover la llave de nuestra cadena
    texto = texto[1:]
    # Aclaracion:
    # Se ingresa el numero 1 por que es su posicion en la cadena ya que la posicion 0 sera nuestra llave.
    textoDes = ""
    # Aqui vamos a hacer el proceso a inversa del cual aplicamos en Encriptado
    for caracter in texto:
        codigo_ascii = ord(caracter)
        if codigo_ascii >= 32 and codigo_ascii <= 126:
            coo = codigo_ascii - int(llave)
            cardes = chr(coo)
            textoDes += cardes
        else:
            textoDes += caracter

    with open(ruta_archivo, 'w') as ar_object:
        ar_object.write(textoDes)


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
                                  command=lambda: encriptar())
button1.pack(pady=20, padx=10)
button1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=frame, text="Desencriptar", width=200, height=50,
                                  command=lambda: desencriptar())
button2.pack(pady=20, padx=10)
button2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()
