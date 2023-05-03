#Programa que contiene la logica de encriptacion
import os
import random
import  tkinter as tk
from tkinter  import filedialog
#Primero vamos a generar el numero random entre 1 y 10
llave = random.randint(1,10)

ventana = tk.Tk()

ruta_archivo = filedialog.askopenfilename()

print(ruta_archivo)
with open(ruta_archivo) as ar_object:
    texto = ar_object.read()
    print(texto)
#Una vez leido el archivo en la cadena
#Lo remplazamos con el encriptado con un for que recorrera esa cadena
encriptado = []

for caracter in texto:
    encriptado.append(str(ord(caracter) + llave))

#Para desencriptarlo necesitamos la funcion char("Valor entero")// Chicos si ven esto borrenlo
texto2= ""
for caracter in encriptado:
    texto2 +=chr(int(caracter))

#Ahora procederemos a modificar nuestro archivo de texto base

with open(ruta_archivo,'w') as ar_object:
   ar_object.write(texto2)
   #Para Este resultado se uso el archivo prueba para crear