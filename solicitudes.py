## EN ESTE MODULO PONEMOS SOLAMENTE LAS FUNCIONES PARA EMPAQUETAR Y ENVIAR LA SOLICITUD COMPLETA
# Flujo 1: Generar solicitud
from archivos import guardar_solicitud_csv, obtener_proximo_id


def generar_solicitud(estado_usuario):

    # 1. Le pedimos al archivo que calcule el ID que corresponde
    nuevo_id = obtener_proximo_id()

    # 2. Armamos el diccionario
    diccionario_solicitud = {
        "id_solicitud": nuevo_id,
        "DNI_solicitante": estado_usuario["dni"],
        "tipo_de_licencia": estado_usuario["categoria"],
        "fecha_inicio": estado_usuario["fecha_inicio"],
        "dias_solicitados": estado_usuario["dias_solicitados"],
        "descripcion_solicitud": estado_usuario["descripcion_solicitud"],
        "estado_solicitud": "ingresada",
    }

    # 3. Lo mandamos a guardar
    guardar_solicitud_csv(diccionario_solicitud)

    return True
