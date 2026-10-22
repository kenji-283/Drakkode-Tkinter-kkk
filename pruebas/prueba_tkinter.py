import tkinter as tk

ventana = tk.Tk()

ventana.title("Prueba de Drakkode por kenji")
ventana.geometry("700x600")
ventana.configure(bg="#08102E")

ventana.resizable(False, False)

titulo = tk.Label(
ventana, text="DRAKKODE PRUEBA", 
font=("Arial", 24, "bold"),
bg="#08102E", 
fg="#2F7EF7")

titulo.pack(pady=40)

etiqueta1= tk.Label(ventana,
text="Correo Electronico",
font=("Arial",10, "bold"),
bg="#08102F",
fg="#2F7EF7")

etiqueta1.pack(pady=5)

entrada1= tk.Entry(ventana,
width=30)

entrada1.pack(pady=5)

etiqueta2= tk.Label(ventana,
text="Contraseña",
font=("Arial",10, "bold"),
bg="#08102F",
fg="#2F7EF7")

etiqueta2.pack(pady=5)

entrada2= tk.Entry(ventana,
width=30)

entrada2.pack(pady=5)

mensajek= tk.Label(ventana, 
text="Esto es una prueba de uso hecha por kenji", 
font=("Arial", 10),
bg="#08102E", 
fg="#FFFFFF")

botonreg= tk.Button(ventana,
text="Registrar", 
font=("Arial", 10),
bg="#08103E",
fg="#FFFFFF")

botonin= tk.Button(ventana,
text="Iniciar Sesión",
font=("Arial",10, "bold"),
bg="#08103F",
fg="#FFFFFF")

etiqueta1.pack(pady=5)

entrada1= tk.Entry(ventana,
width=30)

entrada1.pack(pady=5)

mensajek.pack()
botonreg.pack(pady=5, side="left")
botonin.pack(pady=5, side="right")

mensajereg= tk.Label(ventana,
text="No tienes cuenta?, Registrate!",
bg="#08101E",
fg="#FFFFFF")

mensajereg.pack()
ventana.mainloop()
#supongo que sale mejor usar un grid que un pack para organizar los elementos :v .
#Eliesker pide utilizar modularidad asi que voy a usar clases para separar todo lo que :p pide
