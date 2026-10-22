from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nombre: str
    contraseña: str
    rol: str
    activo: bool = True


@dataclass
class Proyecto:
    id: int
    nombre: str
    descripcion: str
    cliente_id: int
    desarrollador_id: int
    estado: str
    costo: float
