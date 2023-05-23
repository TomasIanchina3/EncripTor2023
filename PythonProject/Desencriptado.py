#Programa que contiene la logica de desencriptacion
from tkinter import filedialog

def desencriptar():

    ruta_archivo = filedialog.askopenfilename()

    print(ruta_archivo)
    with open(ruta_archivo) as ar_object:
        texto = ar_object.read()
    #Aqui se repite el proceso de encriptado pero esta vez vamos a realizar las siguientes operaciones.
    #1° Debemos identificar nuestra llave
    llave = texto[0]
    #2° Vamos a remover la llave de nuestra cadena
    texto = texto[1:]
    #Aclaracion:
    #Se ingresa el numero 1 por que es su posicion en la cadena ya que la posicion 0 sera nuestra llave.
    textoDes = ""
    #Aqui vamos a hacer el proceso a inversa del cual aplicamos en Encriptado
    for caracter in texto:
        codigo_ascii = ord(caracter)
        if codigo_ascii >=32 and codigo_ascii <= 126:
            coo = codigo_ascii - int(llave)
            cardes = chr(coo)
            textoDes += cardes
        else:
            textoDes +=caracter


    with open(ruta_archivo,'w') as ar_object:
        ar_object.write(textoDes)