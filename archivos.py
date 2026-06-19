import csv
import os

ARCHIVOS_EMPLEADOS = "data/datos_empleados.csv"
ARCHIVOS_SOLICITUDES = "data/solicitudes_dias.csv"
ARCHIVO_SESIONES = "data/sesiones_pendientes.csv"


def buscar_empleado(dni):  # Devuelve el dict del empleado o None si no existe"
    try:
        with open(ARCHIVOS_EMPLEADOS, mode="r", encoding="utf-8") as archivo:
            # Usamos DictReader para leer las filas como diccionarios usando el encabezado
            lector = csv.DictReader(archivo)

            for fila in lector:
                if int(fila["dni_empleado"]) == dni:
                    return fila  # Retorna el diccionario con los datos del empleado
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVOS_EMPLEADOS}.")
    except ValueError:
        print("Error: El formato de DNI en el archivo CSV no es válido.")

    return None


def actualizar_dias_empleado(
    dni, nuevos_dias
):  # Actualiza los dias disponibles de un empleado"
    with open(ARCHIVOS_EMPLEADOS, "r", encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))

    for fila in filas:
        if int(fila["dni_empleado"]) == dni:
            fila["dias_disponibles"] = nuevos_dias

    with open(ARCHIVOS_EMPLEADOS, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(
            archivo,
            fieldnames=["dni_empleado", "nombre", "apellido", "dias_disponibles"],
        )
        writer.writeheader()
        writer.writerows(filas)


def buscar_solicitud(dni):  # Devuelve la solicitud mas reciente de un empleado o None
    encontrada = None
    with open(
        ARCHIVOS_SOLICITUDES, "r", encoding="utf-8"
    ) as archivo:  # El "utf-8" es para que soporte tildes, ñ y caracteres especiales.
        for fila in csv.DictReader(archivo):
            if int(fila["DNI_solicitante"]) == dni:
                encontrada = fila
    return encontrada


def guardar_solicitud_csv(diccionario_solicitud):
    """
    Recibe el diccionario de la solicitud y lo guarda al final del archivo CSV.
    Si el archivo no existe, lo crea y le pone los encabezados.
    """

    # Definimos las columnas exactamente como las pediste
    columnas = [
        "id_solicitud",
        "DNI_solicitante",
        "tipo_de_licencia",
        "fecha_inicio",
        "dias_solicitados",
        "descripcion_solicitud",
        "estado_solicitud",
    ]

    # Verificamos si el archivo ya existe antes de abrirlo
    archivo_existe = os.path.exists(ARCHIVOS_SOLICITUDES)

    # Abrimos en modo "a" (append) para agregar al final sin borrar lo anterior
    with open(ARCHIVOS_SOLICITUDES, mode="a", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)

        # Si el archivo es nuevo, primero le escribimos la fila de encabezados
        if not archivo_existe:
            escritor.writeheader()

        # Finalmente, guardamos los datos
        escritor.writerow(diccionario_solicitud)


def obtener_proximo_id():
    """
    Lee el archivo de solicitudes y devuelve el siguiente número de ID disponible.
    """

    if not os.path.exists(ARCHIVOS_SOLICITUDES):
        return 1  # Si no hay archivo, empezamos por el ID 1

    ultimo_id = 0
    with open(ARCHIVOS_SOLICITUDES, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                # Convertimos a entero para comparar
                id_actual = int(fila["id_solicitud"])
                if id_actual > ultimo_id:
                    ultimo_id = id_actual
            except ValueError:
                pass  # Ignoramos si hay alguna fila rota o vacía

    return ultimo_id + 1


def consultar_saldo_dias(dni):  # Devuelve el dict del empleado o None si no existe"
    try:
        with open(ARCHIVOS_EMPLEADOS, mode="r", encoding="utf-8") as archivo:
            # Usamos DictReader para leer las filas como diccionarios usando el encabezado
            lector = csv.DictReader(archivo)

            for fila in lector:
                # consultamos los dias que tenga ese empleado
                if int(fila["dni_empleado"]) == dni:
                    if fila["dias_disponibles"]:
                        return int(fila["dias_disponibles"])  # retorna los dias
                    else:
                        return  # Retorna none si dias es 0
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVOS_EMPLEADOS}.")
    except ValueError:
        print("Error: El formato de DNI en el archivo CSV no es válido.")

    return None


### LOGICA PARA GUARDAR EL ESTADO ACTUAL DE UNA SESION INICIADA ###

# Definimos el nombre del archivo y las columnas exactas de tu diccionario

CAMPOS_SESION = [
    "etapa",
    "dni",
    "nombre_empleado",
    "apellido_empleado",
    "categoria",
    "descripcion_solicitud",
    "dias_disponibles",
    "dias_solicitados",
    "fecha_inicio",
]


def guardar_sesion(estado_usuario):
    """
    Guarda el estado actual del usuario en el CSV. Si el DNI ya tiene
    una sesión guardada, la actualiza. Si no, agrega una nueva fila.
    """
    sesiones_existentes = []

    # 1. Leemos las sesiones previas (si el archivo existe)
    if os.path.exists(ARCHIVO_SESIONES):
        with open(ARCHIVO_SESIONES, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            sesiones_existentes = list(lector)

    # 2. Buscamos si el DNI ya estaba guardado para actualizarlo
    dni_actual = str(estado_usuario["dni"])
    actualizado = False

    for i, sesion in enumerate(sesiones_existentes):
        if sesion["dni"] == dni_actual:
            sesiones_existentes[i] = estado_usuario  # Pisamos los datos viejos
            actualizado = True
            break

    # 3. Si no lo encontró, lo agregamos como una sesión nueva
    if not actualizado:
        sesiones_existentes.append(estado_usuario)

    # 4. Sobrescribimos el archivo con la lista actualizada
    with open(ARCHIVO_SESIONES, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_SESION)
        escritor.writeheader()
        escritor.writerows(sesiones_existentes)


def recuperar_sesion(dni):
    """
    Busca si existe una sesión inconclusa para el DNI ingresado.
    Retorna el diccionario de estado si lo encuentra, o None si no hay sesión.
    """
    if not os.path.exists(ARCHIVO_SESIONES):
        return None

    with open(ARCHIVO_SESIONES, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for sesion in lector:
            if sesion["dni"] == str(dni):
                # Importante: CSV guarda todo como texto. Si tenías valores vacíos,
                # los transforma en strings vacíos ("").
                return sesion

    return None


def eliminar_sesion(dni):
    """
    Borra la sesión del usuario una vez que el trámite finalizó exitosamente.
    """
    if not os.path.exists(ARCHIVO_SESIONES):
        return

    # Leemos todas las filas menos la del DNI que queremos borrar
    sesiones_restantes = []
    with open(ARCHIVO_SESIONES, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for sesion in lector:
            if sesion["dni"] != str(dni):
                sesiones_restantes.append(sesion)

    # Reescribimos el archivo sin esa fila
    with open(ARCHIVO_SESIONES, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_SESION)
        escritor.writeheader()
        escritor.writerows(sesiones_restantes)
