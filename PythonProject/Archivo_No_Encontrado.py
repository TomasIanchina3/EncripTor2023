from os import open

nombre = 'archivoNoExiste.txt'
try:
with open(nombre) as objt_a:
    contenido = objt_a.read()
except FileNotFoundError:
mensaje="ERROR Archivo no encotrado"
print(mensaje)