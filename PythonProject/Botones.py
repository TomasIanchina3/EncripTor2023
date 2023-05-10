import tkinter as tk

class BarraMenu(tk.Tk):

    def __init__(self):
        super().__init__()

        self.run()
    def run(self):
        menu_prin = tk.Menu(self)
        menu_arch = tk.Menu(menu_prin, tearoff=0)
        menu_arch.add_command(label="Encriptar archivo.")
        menu_arch.add_command(label="Desencriptar archivo.")
        menu_arch.add_command(label="Abrir archivo.")
        menu_arch.add_command(label="Guardar archivo.")
        menu_arch.add_command(label="Guardar como...")
        menu_prin.add_command(label="Salir", command=self.destroy)
        menu_prin.add_cascade(label="Acerca de...")
        menu_prin.add_cascade(label="Archivo", menu=menu_arch)
        self.config(menu=menu_prin)

def main():
    app = BarraMenu()
    app.mainloop()

if __name__ == '__main__':
    main()