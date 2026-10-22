import tkinter as tk
from tkinter import messagebox

from operaciones import OperacionesDrakkode


class AplicacionDrakkode:
    def __init__(self, ventana):
        self.ventana = ventana
        self.operaciones = OperacionesDrakkode()
        self.usuario_actual = None

        #Ajustes de la ventana en tkinter
        self.ventana.title("Drakkode: Software y Tecnologias")
        #titulo de la ventana
        self.ventana.geometry("900x1050")
        #tamaño de la ventana
        self.ventana.resizable(True, True)
        #configuracion de escala de la ventana, por defecto en falso,se puede cambiar
        self.ventana.config(bg="#08102E")
        #color de la ventana, rgb hexadecimal, azul oscuro
        self.mostrar_login()
        #mostrar el login obviamente
		
    def limpiar_ventana(self):
        #Ocultar todos los elementos para mostrar otra pagina
        for elemento in self.ventana.winfo_children():
            elemento.destroy()

    def mostrar_login(self):
        #Titulooooo
        self.titulo = tk.Label(self.ventana, text="DRAKKODE",
            font=("Arial", 24, "bold"), bg="#08102E", fg="#2F7EF7")
        self.titulo.pack(pady=(35, 5))
		
        #Subtitulo
        self.subtitulo = tk.Label(self.ventana, text="SOFTWARE Y TECNOLOGIAS",
            font=("Arial", 10, "bold"), bg="#08102E", fg="#2F7EF7")
        self.subtitulo.pack(pady=(0, 25))

        #panel del formulario
        self.form_log = tk.Frame(self.ventana, bg="#0F1D34")
        self.form_log.pack(padx=40, fill="x")
        #scrolllbar

        #Subtitulo
        self.subtitulo3 = tk.Label(self.form_log, text="Iniciar sesión",
            font=("Arial", 8, "bold"), bg="#08102E", fg="#2F7EF7")
        self.subtitulo3.pack(pady=(0, 10))

        #etiquetas del usuario
        self.etiqueta1 = tk.Label(self.form_log, text="Correo Electronico",
            font=("Arial", 10, "bold"), bg="#0F1D34", fg="#FFFFFF")
        self.etiqueta1.pack(pady=(0, 5), padx=20, anchor="w")

        #entrada del usuario, entry
        self.entrada1 = tk.Entry(self.form_log, width=30, font=("Arial", 11),
            bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat")
        self.entrada1.pack(fill="x", padx=20, ipady=8)

        #etiqueta de contraseña
        self.etiqueta2 = tk.Label(self.form_log, text="Contraseña",
            font=("Arial", 10, "bold"), bg="#0F1D34", fg="#FFFFFF")
        self.etiqueta2.pack(pady=(12, 5), padx=20, anchor="w")

        #entrada de contraseña
        self.entrada2 = tk.Entry(self.form_log, width=30, font=("Arial", 11),
            bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat", show="X")
        self.entrada2.pack(fill="x", padx=20, ipady=8)

        #Mensaje de registrarse!!!
        self.mensajereg = tk.Label(self.form_log, text="No tienes cuenta?, Registrate!",
            bg="#08101E", fg="#FFFFFF")
        #boton de inicio de sesion
        self.botonin = tk.Button(self.form_log, text="Iniciar Sesión",
            font=("Arial", 10, "bold"), bg="#08103F", fg="#FFFFFF",
            cursor="hand2", command=self.iniciar_sesion)
        self.botonin.pack(padx=20, pady=(30, 15), ipady=8)
        self.mensajereg.pack(pady=(5, 10))

        #boton de registrarse
        self.botonreg = tk.Button(self.form_log, text="Registrarse",
            font=("Arial", 10), bg="#08103E", fg="#FFFFFF",
            cursor="hand2", command=self.pagina_reg)
        self.botonreg.pack(pady=(0, 25), padx=20, ipady=8)

        nota = tk.Label(self.ventana, text="Construye, innova, evoluciona",
            font=("Arial", 9), bg="#08102E", fg="#B8C5D9")
        nota.pack(pady=15)

    #metodo de inicio de sesion
    def iniciar_sesion(self):
        usuario = self.entrada1.get().strip()
        contraseña = self.entrada2.get()
        #variables de inicio de sesion
        if usuario == "" or contraseña == "":
            messagebox.showwarning("Campos vacios", "Introduce tu correo y contraseña.")
            return

        usuario_encontrado = self.operaciones.iniciar_sesion(usuario, contraseña)
        if usuario_encontrado is None:
            messagebox.showerror("Acceso denegado", "El correo o la contraseña son incorrectos.")
            return
        self.usuario_actual = usuario_encontrado
        self.mostrar_panel()

    #funcion de registro, crea una nueva ventana
    def pagina_reg(self):
        #ocultar el formulario anterior de inicio para mostrar el de registro
        self.form_log.pack_forget()
        self.form_reg = tk.Frame(self.ventana, bg="#0F1D34")
        self.form_reg.pack(padx=40, fill="x")
		
        #Subtitulo
        self.subtitulo2 = tk.Label(self.form_reg, text="Registrarse",
            font=("Arial", 8, "bold"), bg="#08102E", fg="#2F7EF7")
        self.subtitulo2.pack(pady=(0, 10))

        #etiquetas del usuario
        self.etiqueta22 = tk.Label(self.form_reg, text="Correo Electronico",
            font=("Arial", 10, "bold"), bg="#0F1D34", fg="#FFFFFF")
        self.etiqueta22.pack(pady=(0, 5), padx=20, anchor="w")

        #entrada del usuario, entry
        self.entrada11 = tk.Entry(self.form_reg, width=30, font=("Arial", 11),
            bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat")
        self.entrada11.pack(fill="x", padx=20, ipady=8)

        #etiqueta de contraseña
        self.etiqueta3 = tk.Label(self.form_reg, text="Contraseña",
            font=("Arial", 10, "bold"), bg="#0F1D34", fg="#FFFFFF")
        self.etiqueta3.pack(pady=(10, 5), padx=20, anchor="w")

        #entrada del usuario, entry
        self.entrada3 = tk.Entry(self.form_reg, width=30, font=("Arial", 11),
            bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat", show="X")
        self.entrada3.pack(fill="x", padx=20, ipady=8)

        #confirmar contraseña
        self.etiqueta3conf = tk.Label(self.form_reg, text="Confirma tu contraseña",
            font=("Arial", 10, "bold"), bg="#0F1D34", fg="#FFFFFF")
        self.etiqueta3conf.pack(pady=(10, 5), padx=20, anchor="w")

        #entrada para confirmar la contraseña
        self.entrada3conf = tk.Entry(self.form_reg, width=30, font=("Arial", 11),
            bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat", show="X")
        self.entrada3conf.pack(fill="x", padx=20, ipady=8)

        #Mensaje de registrarse!!!
        self.mensajereg2 = tk.Label(self.form_reg, text="Haz llenado los campos, toca registrar, regresa para iniciar sesion!",
            bg="#08101E", fg="#FFFFFF")

        self.botonvolv = tk.Button(self.form_reg, text="Volver", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.volver_log)
        #Se conserva el orden visual del formulario que ya estaba hecho
        self.botonvolv.pack(padx=20, pady=(5, 5), ipady=8)
        self.mensajereg2.pack(pady=(5, 5))

        #boton de registrarse
        self.botonreg2 = tk.Button(self.form_reg, text="Registrarse", font=("Arial", 10),
            bg="#08103E", fg="#FFFFFF", cursor="hand2", command=self.registrar_usuario)
        self.botonreg2.pack(padx=20, pady=(5, 5), ipady=8)

    def volver_log(self):
        #destruir el formulario de registro
        self.form_reg.destroy()
        #mostrar el formulario de login
        self.form_log.pack(padx=40, fill="x")

    def registrar_usuario(self):
        #definir los usuarios y las contraseñas
        usuario = self.entrada11.get().strip()
        contraseña = self.entrada3.get()
        confirmar = self.entrada3conf.get()
        #variables de registro
        if usuario == "" or contraseña == "" or confirmar == "":
            messagebox.showwarning("Campos vacios", "Introduce tu correo y confirma tu contraseña para registrar.")
            return
        if "@" not in usuario or "." not in usuario.split("@")[-1]:
            messagebox.showwarning("Correo no valido", "Introduce un correo electronico valido.")
            return
        if contraseña != confirmar:
            messagebox.showwarning("Error!", "Las contraseñas no coinciden :p !!")
            return
        if len(contraseña) < 4:
            messagebox.showwarning("Contraseña corta", "Usa al menos 4 caracteres para esta demostracion.")
            return

        correcto, mensaje = self.operaciones.registrar_usuario(usuario, contraseña)
        if correcto:
            messagebox.showinfo("Registro completo", mensaje)
            self.volver_log()
            self.entrada1.delete(0, tk.END)
            self.entrada1.insert(0, usuario)
            self.entrada2.focus_set()
        else:
            messagebox.showerror("No se pudo registrar", mensaje)

    def mostrar_panel(self):
        self.limpiar_ventana()
        #Titulo del panel principal
        tk.Label(self.ventana, text="DRAKKODE", font=("Arial", 24, "bold"),
            bg="#08102E", fg="#2F7EF7").pack(pady=(22, 3))
        tk.Label(self.ventana, text=f"Bienvenido: {self.usuario_actual.nombre} | {self.usuario_actual.rol}",
            font=("Arial", 10, "bold"), bg="#08102E", fg="#FFFFFF").pack(pady=(0, 12))

        #Panel de opciones
        panel = tk.Frame(self.ventana, bg="#0F1D34")
        panel.pack(fill="both", expand=True, padx=25, pady=8)
        tk.Label(panel, text="Panel de proyectos", font=("Arial", 15, "bold"),
            bg="#0F1D34", fg="#2F7EF7").pack(pady=12)

        tk.Button(panel, text="Ver todos los proyectos", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.ver_proyectos).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Registrar nuevo proyecto", font=("Arial", 10, "bold"),
            bg="#2F7EF7", fg="#FFFFFF", cursor="hand2", command=self.ventana_nuevo_proyecto).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Buscar proyecto (busqueda lineal)", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.ventana_buscar).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Ver cola de solicitudes", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.ver_cola).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Atender siguiente solicitud (FIFO)", font=("Arial", 10, "bold"),
            bg="#E63946", fg="#FFFFFF", cursor="hand2", command=self.atender_cola).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Ver grafo de clientes y proyectos", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.ver_grafo).pack(fill="x", padx=35, pady=5, ipady=5)
        tk.Button(panel, text="Cerrar sesion", font=("Arial", 10, "bold"),
            bg="#08103F", fg="#FFFFFF", cursor="hand2", command=self.cerrar_sesion).pack(fill="x", padx=35, pady=(18, 12), ipady=5)

        self.resumen = tk.Label(self.ventana, text="", font=("Arial", 9),
            bg="#08102E", fg="#B8C5D9")
        self.resumen.pack(pady=8)
        self.actualizar_resumen()

    def actualizar_resumen(self):
        if hasattr(self, "resumen") and self.resumen.winfo_exists():
            self.resumen.config(text=f"Proyectos: {len(self.operaciones.proyectos)}   |   Solicitudes en cola: {len(self.operaciones.cola)}")

    def ver_proyectos(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Proyectos de Drakkode")
        ventana.geometry("560x450")
        ventana.configure(bg="#08102E")
        tk.Label(ventana, text="Lista de proyectos", font=("Arial", 15, "bold"),
            bg="#08102E", fg="#2F7EF7").pack(pady=10)
        lista = tk.Listbox(ventana, width=70, height=19, bg="#162640", fg="#FFFFFF",
            selectbackground="#2F7EF7")
        lista.pack(fill="both", expand=True, padx=15, pady=10)
        for proyecto in self.operaciones.obtener_proyectos():
            lista.insert(tk.END, f"#{proyecto.id} | {proyecto.nombre} | C$ {proyecto.costo:.2f} | {proyecto.estado}")

    def ventana_nuevo_proyecto(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar proyecto")
        ventana.geometry("460x430")
        ventana.configure(bg="#08102E")
        tk.Label(ventana, text="Registrar nuevo proyecto", font=("Arial", 14, "bold"),
            bg="#08102E", fg="#2F7EF7").pack(pady=12)
        tk.Label(ventana, text="Nombre del proyecto", bg="#08102E", fg="#FFFFFF").pack(anchor="w", padx=25)
        nombre = tk.Entry(ventana, width=45, bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF")
        nombre.pack(padx=25, pady=5, ipady=5)
        tk.Label(ventana, text="Descripcion", bg="#08102E", fg="#FFFFFF").pack(anchor="w", padx=25)
        descripcion = tk.Text(ventana, width=42, height=5, bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF")
        descripcion.pack(padx=25, pady=5)
        tk.Label(ventana, text="Costo estimado en cordobas", bg="#08102E", fg="#FFFFFF").pack(anchor="w", padx=25)
        costo = tk.Entry(ventana, width=20, bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF")
        costo.pack(padx=25, pady=5)

        def guardar():
            if not nombre.get().strip() or not descripcion.get("1.0", tk.END).strip() or not costo.get().strip():
                messagebox.showwarning("Campos vacios", "Completa todos los campos.", parent=ventana)
                return
            try:
                valor = float(costo.get())
                if valor < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Costo incorrecto", "Introduce un costo numerico mayor o igual a cero.", parent=ventana)
                return
            proyecto = self.operaciones.agregar_proyecto(nombre.get(), descripcion.get("1.0", tk.END).strip(), self.usuario_actual.id, valor)
            messagebox.showinfo("Proyecto guardado", f"Se registro el proyecto #{proyecto.id} y se agrego a la cola.", parent=ventana)
            ventana.destroy()
            self.actualizar_resumen()

        tk.Button(ventana, text="Guardar proyecto", command=guardar, bg="#2F7EF7", fg="#FFFFFF",
            cursor="hand2", font=("Arial", 10, "bold")).pack(pady=12, ipady=5)

    def ventana_buscar(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Buscar proyecto")
        ventana.geometry("500x300")
        ventana.configure(bg="#08102E")
        tk.Label(ventana, text="Busqueda lineal de proyectos", font=("Arial", 14, "bold"),
            bg="#08102E", fg="#2F7EF7").pack(pady=15)
        tk.Label(ventana, text="Escribe parte del nombre o descripcion:", bg="#08102E", fg="#FFFFFF").pack()
        entrada = tk.Entry(ventana, width=45, bg="#162640", fg="#FFFFFF", insertbackground="#FFFFFF")
        entrada.pack(pady=10, ipady=5)
        resultado = tk.Label(ventana, text="", justify="left", wraplength=440, bg="#08102E", fg="#FFFFFF")
        resultado.pack(padx=20, pady=10)

        def buscar():
            proyecto = self.operaciones.buscar_proyecto(entrada.get())
            if proyecto is None:
                resultado.config(text="No se encontro ningun proyecto con ese texto.")
            else:
                resultado.config(text=f"ID: {proyecto.id}\nNombre: {proyecto.nombre}\nDescripcion: {proyecto.descripcion}\nEstado: {proyecto.estado}\nCosto: C$ {proyecto.costo:.2f}")
        tk.Button(ventana, text="Buscar", command=buscar, bg="#2F7EF7", fg="#FFFFFF").pack()

    def ver_cola(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Cola de solicitudes")
        ventana.geometry("560x420")
        ventana.configure(bg="#08102E")
        tk.Label(ventana, text="Cola de solicitudes (primero en entrar, primero en salir)",
            font=("Arial", 12, "bold"), bg="#08102E", fg="#2F7EF7", wraplength=520).pack(pady=12)
        lista = tk.Listbox(ventana, width=68, height=17, bg="#162640", fg="#FFFFFF")
        lista.pack(fill="both", expand=True, padx=15, pady=10)
        for posicion, proyecto in enumerate(self.operaciones.obtener_cola(), start=1):
            lista.insert(tk.END, f"{posicion}. #{proyecto.id} - {proyecto.nombre}")
        if not self.operaciones.cola:
            lista.insert(tk.END, "No hay solicitudes pendientes en la cola.")

    def atender_cola(self):
        proyecto = self.operaciones.procesar_siguiente()
        if proyecto is None:
            messagebox.showinfo("Cola vacia", "No hay solicitudes pendientes para atender.")
        else:
            messagebox.showinfo("Solicitud atendida", f"Se atendio primero el proyecto #{proyecto.id}: {proyecto.nombre}.\nSu estado se actualizo a en desarrollo si estaba pendiente.")
        self.actualizar_resumen()

    def ver_grafo(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Grafo de clientes y proyectos")
        ventana.geometry("570x500")
        ventana.configure(bg="#08102E")
        tk.Label(ventana, text="Grafo bipartito: clientes - proyectos", font=("Arial", 13, "bold"),
            bg="#08102E", fg="#2F7EF7").pack(pady=10)
        lienzo = tk.Canvas(ventana, width=540, height=330, bg="#0F1D34", highlightthickness=0)
        lienzo.pack(padx=10, pady=5)
        grafo = self.operaciones.obtener_grafo()
        clientes = list(grafo.keys())
        proyectos = [(cliente, proyecto) for cliente, lista in grafo.items() for proyecto in lista]
        if not clientes:
            lienzo.create_text(270, 160, text="No hay proyectos para representar", fill="white")
        else:
            #Dibujar nodos de clientes a la izquierda y proyectos a la derecha
            posiciones_cliente = {}
            for i, cliente in enumerate(clientes):
                y = 35 + i * (260 // max(1, len(clientes)))
                posiciones_cliente[cliente] = (90, y)
                lienzo.create_oval(35, y-16, 145, y+16, fill="#2F7EF7", outline="white")
                lienzo.create_text(90, y, text=cliente, fill="white", font=("Arial", 8, "bold"))
            cantidad = max(1, len(proyectos))
            for i, (cliente, proyecto) in enumerate(proyectos):
                y = 20 + i * (290 // cantidad)
                x1, y1 = posiciones_cliente[cliente]
                lienzo.create_line(x1+55, y1, 385, y, fill="#B8C5D9", width=1)
                lienzo.create_rectangle(385, y-12, 535, y+12, fill="#162640", outline="#2F7EF7")
                lienzo.create_text(460, y, text=proyecto[:24], fill="white", font=("Arial", 7))
        tk.Label(ventana, text="Lista de adyacencia:", bg="#08102E", fg="#FFFFFF", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=(8, 0))
        texto = tk.Text(ventana, height=5, width=65, bg="#162640", fg="#FFFFFF")
        texto.pack(padx=15, pady=5)
        for cliente, lista in grafo.items():
            texto.insert(tk.END, f"{cliente} -> {', '.join(lista)}\n")
        texto.config(state="disabled")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.limpiar_ventana()
        self.mostrar_login()
