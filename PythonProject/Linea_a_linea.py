nombre_Archivo = './prueba_git.txt'
with open(nombre_Archivo) as objecto_A:
    lineas = objecto_A.readlines()

 for line in lineas:
     print(line.rstrip())

#Este metodo funciona para leer el archivo linea por linea