#El metodo de aca abajo es para abrir,leer y mostrar el archivo
#Se utiliza el metodo with para cerrar automaticamente el archivo
#Pero se debe crear como un objeto el contenido del mismo como se ve mas abajo
with open('./prueba_git.txt') as objeto_Archivo:
    contenido = objeto_Archivo.read()
    print(contenido)


