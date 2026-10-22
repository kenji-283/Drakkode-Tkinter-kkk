DRAKKODE - Proyecto academico Tkinter
====================================

REQUISITOS
- Python 3
- Tkinter (Se instala como extension en VS Code para Windows, si se utiliza otro editor o Sistema Operativo como linux, verifica si tienes instalado el paquete de tkinter para Python3 instalado, mediante pip)
- No requiere instalar paquetes externos(almenos que uses linux o otros IDEs que no posean la biblioteca Tkinter).

EJECUCION
1. Descomprime el ZIP.
2. Entra en la carpeta Drakkode-Tkinter-kkk-main.
3. Ejecuta: python3 main.py

CUENTAS INICIALES ACTIVAS (solo para demostracion)
- adminKENji@drakkode.com / admin123
- cliente@drakkode.com / cliente123

FUNCIONALIDADES
- Registro real de usuarios y almacenamiento en datos/usuarios.json.
- Inicio de sesion consultando usuarios guardados.
- Clases dataclass Usuario y Proyecto.
- Lista de objetos Proyecto.
- Busqueda lineal por nombre o descripcion.
- Cola FIFO de proyectos pendientes, guardada en datos/cola_solicitudes.jsonl.
- Registrar y listar proyectos.
- Atender la siguiente solicitud y actualizar su estado.
- Grafo bipartido simplificado Cliente-Proyecto y lista de adyacencia.
- Modularidad: modelos.py, almacenamiento.py, operaciones.py, interfaz.py y main.py.

ARCHIVOS DE DATOS
- usuarios.json contiene seis registros de demostracion; solo los dos primeros estan activos para el inicio de sesion. Los otros cuatro sirven como datos de ejemplo inactivos para demostrar seis objetos Usuario. Los usuarios nuevos registrados quedan activos.
- proyectos.json contiene seis objetos Proyecto de ejemplo.
- cola_solicitudes.jsonl contiene una solicitud JSON por linea. La cola se procesa en orden FIFO.

NOTA ACADEMICA Y SEGURIDAD DE LOS USUARIOS DE PRUEBA
Este proyecto almacena contrasenas en texto plano para mantenerlo sencillo como demostracion local. No debe utilizarse para cuentas reales. Un sistema real debe guardar hashes de contrasenas, no las contrasenas originales.

Los archivos JSON y JSONL se actualizan al registrar usuarios, crear proyectos o atender solicitudes. Si quieres reiniciar los datos, cierra la aplicacion y restaura los archivos originales del ZIP.
