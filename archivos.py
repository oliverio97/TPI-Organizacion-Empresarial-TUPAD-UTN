import csv
import os

ARCHIVOS_EMPLEADOS = "data/datos_empleados.csv"
# ARCHIVO_SALICITUDES = "solicitudes_dias.csv"


#def inicializar_csv():  # Crea los CSVs con encabezados y datos si no existen" - Puede que ni haga falta poner esta funcion
#    pass


def buscar_empleado(dni):  # Devuelve el dict del empleado o None si no existe"
    try:
        with open(ARCHIVOS_EMPLEADOS, mode="r", encoding="utf-8") as archivo:
            # Usamos DictReader para leer las filas como diccionarios usando el encabezado
            lector = csv.DictReader(archivo)

            for fila in lector:
                # Suponiendo que la columna en tu CSV se llama 'dni' o 'DNI'
                if int(fila["dni_empleado"]) == dni:
                    return fila  # Retorna el diccionario con los datos del empleado
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVOS_EMPLEADOS}.")
    except ValueError:
        print("Error: El formato de DNI en el archivo CSV no es válido.")

    return None


def actualizar_dias_empleado(dni, nuevos_dias):  # Actualiza los dias disponibles de un empleado"
    with open ("datos_emplados.csv", "r", encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))
    
    for fila in filas:
        if int(fila["DNI_empleado"]) ==dni:
            fila["dias_disponibles"] = nuevos_dias
    
    with open ("datos_empleados.csv", "w", newline = "", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames = ["DNI_empleado", "nombre", "apellido", "dias_disponibles"])
        writer.writeheader()
        writer.writerows(filas)


def generar_id():  # Genera un ID para nuevas solicitudes
    with open("solicitudes_dias,csv", "r", encoding="utf-8") as archivo:
        filas = list(csv.DictReader (archivo))
        if not filas:
            return 1
    ultimo_id = max(int(fila["id_solicitud"]) for fila in filas)
    return ultimo_id + 1


def buscar_solicitud(dni):  # Devuelve la solicitud mas reciente de un empleado o None
    encontrada = None
    with open ("solicitudes_dias.csv", "r", encoding="utf-8") as archivo: #El "utf-8" es para que soporte tildes, ñ y caracteres especiales. 
        for fila in csv.DictReader(archivo):
            if int(fila["DNI_solicitante"]) == dni:
                encontrada = fila
    return encontrada


def guardar_solicitud(dni, tipo_licencia, fecha_inicio, fecha_fin, descripcion):
    with open("solicitudes_dias.csv", "a", newline="", encoding="utf-8") as archivo: #"a" para modo append, agrega al final del archivo sin borrar lo que hay
        writer = csv.DictReader(archivo, fieldnames=[
            "id_solicitud", "DNI_solicitante", "tipo_de_licencia", "fecha_inicio",
            "fecha_finalizacion", "descripcion_solicitud", "estado_solicitud"
        ])
        writer.writerow({
            "id_solicitud":             generar_id(),
            "DNI_solicitante":          dni,
            "tipo_de_licencia":         tipo_licencia,
            "fecha_inicio":             fecha_inicio,
            "fecha_finaliazcion":       fecha_fin,
            "descripcion_solicitud":    descripcion,
            "estado_solicitud":         "pendiente",
        })

#def actualizar_campo_solicitud(dni, campo, nuevo_valor):
#    pass  # Modifica un campo de la solicitud más reciente de un empleado. tipo_de_licencia, fecha_inicio, fecha_finalizacion,descripcion_solicitud, estado_solicitud
