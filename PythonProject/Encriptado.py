#Programa que contiene la logica de encriptacion
import random
from tkinter import filedialog

def encriptar():
    #Primero vamos a generar el numero random entre 1 y 4
    llave = random.randint(1,4)

    ruta_archivo = filedialog.askopenfilename()

    print(ruta_archivo)
    with open(ruta_archivo) as ar_object:
        texto = ar_object.read()

    #Una vez leido el archivo en la cadena
    #Lo remplazamos con el encriptado con un for que recorrera esa cadena
    encriptado = ""
    #Al ser la version beta este solo admitira el codigo ASCII pero no el codigo ASCII extendido ya que deberiamos aplicar UNICODE derivando en otro metodo distinto
    for caracter in texto:
        codigoa = ord(caracter)
        if codigoa >= 32 and codigoa <= 122:
          ce = codigoa + llave
          caracterencriptado = chr(ce)
          encriptado += caracterencriptado
        else:
            encriptado += caracter

    #Ahora procederemos a modificar nuestro archivo de texto base

    with open(ruta_archivo,'w') as ar_object:
        ar_object.write(str(llave))

    with open(ruta_archivo,'a') as ar_object:
        ar_object.write(encriptado)
    #Para Este resultado se uso el archivo prueba para crear
