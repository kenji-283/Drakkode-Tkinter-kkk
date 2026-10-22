import tkinter as tk
from interfaz import AplicacionDrakkode


def main():
    ventana = tk.Tk()
    aplicacion = AplicacionDrakkode(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()

#archivo de inicio, crea un objeto de la clase aplicación
