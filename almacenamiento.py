import json
from dataclasses import asdict
from pathlib import Path
#se utiliza pathlib para encontrar los archivos auqnue no esten en la misma carpeta
from modelos import Usuario, Proyecto

#Esta ruta permite encontrar los archivos aunque se ejecute main.py desde otra carpeta
CARPETA_DATOS = Path(__file__).resolve().parent / "datos"
ARCHIVO_USUARIOS = CARPETA_DATOS / "usuarios.json"
ARCHIVO_PROYECTOS = CARPETA_DATOS / "proyectos.json"
ARCHIVO_COLA = CARPETA_DATOS / "cola_solicitudes.jsonl"


def preparar_archivos():
    #Crear la carpeta y los archivos si todavía no existen
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    if not ARCHIVO_USUARIOS.exists():
        guardar_usuarios([])
    if not ARCHIVO_PROYECTOS.exists():
        guardar_proyectos([])
    if not ARCHIVO_COLA.exists():
        ARCHIVO_COLA.write_text("", encoding="utf-8")


def cargar_usuarios():
    preparar_archivos()
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Usuario(**dato) for dato in datos]
    except (json.JSONDecodeError, TypeError):
        return []


def guardar_usuarios(usuarios):
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump([asdict(usuario) for usuario in usuarios], archivo, indent=4, ensure_ascii=False)


def cargar_proyectos():
    preparar_archivos()
    try:
        with open(ARCHIVO_PROYECTOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Proyecto(**dato) for dato in datos]
    except (json.JSONDecodeError, TypeError):
        return []


def guardar_proyectos(proyectos):
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    with open(ARCHIVO_PROYECTOS, "w", encoding="utf-8") as archivo:
        json.dump([asdict(proyecto) for proyecto in proyectos], archivo, indent=4, ensure_ascii=False)


def cargar_cola():
    #JSONL guarda un objeto JSON por cada linea, ideal para solicitudes de la cola
    preparar_archivos()
    from collections import deque
    cola = deque()
    try:
        with open(ARCHIVO_COLA, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    try:
                        cola.append(Proyecto(**json.loads(linea)))
                    except (json.JSONDecodeError, TypeError):
                        continue
    except FileNotFoundError:
        pass
    return cola


def guardar_cola(cola):
    #Se reemplaza el archivo con el estado actual de la cola
    CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
    with open(ARCHIVO_COLA, "w", encoding="utf-8") as archivo:
        for proyecto in cola:
            archivo.write(json.dumps(asdict(proyecto), ensure_ascii=False) + "\n")
