from collections import deque
from dataclasses import asdict

from modelos import Usuario, Proyecto
from almacenamiento import (
    cargar_usuarios, guardar_usuarios,
    cargar_proyectos, guardar_proyectos,
    cargar_cola, guardar_cola
)


class OperacionesDrakkode:
    def __init__(self):
        self.usuarios = cargar_usuarios()
        self.proyectos = cargar_proyectos()
        self.cola = cargar_cola()
        #La cola se forma con los proyectos pendientes si el archivo JSONL está vacío
        if not self.cola:
            for proyecto in self.proyectos:
                if proyecto.estado == "pendiente":
                    self.cola.append(proyecto)
            guardar_cola(self.cola)

    def registrar_usuario(self, correo, contraseña):
        correo = correo.strip().lower()
        if not correo or not contraseña:
            return False, "Completa todos los campos."
        #Busqueda lineal para evitar registrar el mismo correo dos veces
        for usuario in self.usuarios:
            if usuario.nombre.lower() == correo:
                return False, "Ya existe una cuenta con ese correo."
        nuevo_id = max((usuario.id for usuario in self.usuarios), default=0) + 1
        nuevo_usuario = Usuario(nuevo_id, correo, contraseña, "cliente", True)
        self.usuarios.append(nuevo_usuario)
        guardar_usuarios(self.usuarios)
        return True, "La cuenta se registró correctamente. Ya puedes iniciar sesión."

    def iniciar_sesion(self, correo, contraseña):
        correo = correo.strip().lower()
        #Busqueda lineal en la lista de objetos Usuario
        for usuario in self.usuarios:
            if usuario.nombre.lower() == correo and usuario.contraseña == contraseña and usuario.activo:
                return usuario
        return None

    def buscar_proyecto(self, texto):
        texto = texto.strip().lower()
        if not texto:
            return None
        #Busqueda lineal por nombre o por descripcion
        for proyecto in self.proyectos:
            if texto in proyecto.nombre.lower() or texto in proyecto.descripcion.lower():
                return proyecto
        return None

    def agregar_proyecto(self, nombre, descripcion, cliente_id, costo):
        nuevo_id = max((proyecto.id for proyecto in self.proyectos), default=0) + 1
        proyecto = Proyecto(nuevo_id, nombre.strip(), descripcion.strip(), cliente_id, 0, "pendiente", float(costo))
        self.proyectos.append(proyecto)
        guardar_proyectos(self.proyectos)
        #La cola FIFO guarda objetos Proyecto; el primero que entra es el primero que se atiende
        self.cola.append(proyecto)
        guardar_cola(self.cola)
        return proyecto

    def obtener_proyectos(self):
        return list(self.proyectos)

    def obtener_cola(self):
        return list(self.cola)

    def procesar_siguiente(self):
        if not self.cola:
            return None
        proyecto_cola = self.cola.popleft()
        #Actualizar el objeto que se encuentra en la lista principal
        for proyecto in self.proyectos:
            if proyecto.id == proyecto_cola.id:
                if proyecto.estado == "pendiente":
                    proyecto.estado = "en desarrollo"
                break
        guardar_proyectos(self.proyectos)
        guardar_cola(self.cola)
        return proyecto_cola

    def obtener_grafo(self):
        #Grafo bipartito sencillo: clientes de un lado y proyectos del otro.
        #La lista de adyacencia indica que proyectos pertenecen a cada cliente.
        grafo = {}
        for proyecto in self.proyectos:
            cliente = f"Cliente {proyecto.cliente_id}"
            nombre_proyecto = f"Proyecto {proyecto.id}: {proyecto.nombre}"
            if cliente not in grafo:
                grafo[cliente] = []
            grafo[cliente].append(nombre_proyecto)
        return grafo
