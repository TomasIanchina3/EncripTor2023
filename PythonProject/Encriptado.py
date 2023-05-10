#Programa que contiene la logica de encriptacion
import os
import random
import  tkinter as tk
from tkinter  import filedialog

from more_itertools import run_length

#Primero vamos a generar el numero random entre 1 y 10
llave = random.randint(1,10)

ventana = tk.Tk()

ruta_archivo = filedialog.askopenfilename()

print(ruta_archivo)
with open(ruta_archivo) as ar_object:
    texto = ar_object.read()

#Una vez leido el archivo en la cadena
#Lo remplazamos con el encriptado con un for que recorrera esa cadena
encriptado = ""
#Chicos realice modificaciones este codigo
#Al ser la version beta este solo admitira el codigo ASCII pero no el codigo ASCII extendido ya que deberiamos aplicar UNICODE derivando en otro metodo distinto
for caracter in texto:
<<<<<<< HEAD
    encriptado.append(str(ord(caracter) + llave))

#Para desencriptarlo necesitamos la funcion char("Valor entero")
texto2= ""
for caracter in encriptado:
    texto2 +=chr(int(caracter))
=======
    codigoa = ord(caracter)
    if codigoa >= 32 and codigoa <= 126:
      ce = codigoa + llave
      caracterencriptado = chr(ce)
      encriptado += caracterencriptado
    else:
        encriptado += caracter
>>>>>>> e50105b34dce3d02d12126ad74fd9b5cc814723e

#Ahora procederemos a modificar nuestro archivo de texto base

with open(ruta_archivo,'w') as ar_object:
    ar_object.write(str(llave))

with open(ruta_archivo,'a') as ar_object:
    ar_object.write(encriptado)
   #Para Este resultado se uso el archivo prueba para crear