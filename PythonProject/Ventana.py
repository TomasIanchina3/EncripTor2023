import tkinter as tk
import Encriptado
import Desencriptado

#Creacion ventana
ventana = tk.Tk()
ventana.title("EncripTor 2023")
ventana.config(width=400, height=400)
#Configuracion de menu
menu_prin = tk.Menu()
menu_arch = tk.Menu(menu_prin, tearoff=0)
menu_prin.add_cascade(label="Archivo", menu=menu_arch)
menu_arch.add_command(label="Encriptar archivo.")
menu_arch.add_command(label="Desencriptar archivo.")
menu_arch.add_command(label="Abrir archivo.")
menu_arch.add_command(label="Guardar archivo.")
menu_arch.add_command(label="Guardar como...")
menu_prin.add_cascade(label="Acerca de...")
menu_prin.add_command(label="Salir", command=ventana.destroy)
ventana.config(menu=menu_prin)
#Configuracion botones
boton_encriptar=tk.Button(text="ENCRIPTAR", padx=15, pady=15, command= lambda: Encriptado.encriptar())
boton_encriptar.place(x=150, y=100)
boton_desencriptar=tk.Button(text="DESENCRIPTAR", padx=15, pady=15, command= lambda: Desencriptado.desencriptar())
boton_desencriptar.place(x=150, y=200)

ventana.mainloop()
