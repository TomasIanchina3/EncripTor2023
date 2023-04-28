filename = 'prueba_paraCrear.txt'

with open(filename,'w') as objt_a:
    objt_a.write('Hola chicos soy un archivo creado en python \n')

#si queremos agregar mas de una linea debemos agregar un "\n" al final de cada String que vayamos a agregar.
#Como en casos anteriores utilizamos el bloque with, pero agregamos como parametros una "w"
#Especial cuidado con ese parametro debido a que si ya existe ese archivo lo va a sobreescribir
#Por que lo abre en modo escritura
#Si usamos el parametro "a" este le va a agregar al archivo sin eliminar
# "r+" es para leer y escribir

ejemplos_elementos = ['Jenaro\n','Tomas\n','Franco\n','Gabriel\n']
with open(filename,'a') as objt_a:
    for elementos in ejemplos_elementos:
        objt_a.write(elementos)
