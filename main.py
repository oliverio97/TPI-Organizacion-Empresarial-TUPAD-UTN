# MAQUINA DE ESTADOS DEL PROGRAMA
estado_usuario = {
    "etapa": "inicio",  # inicio / menu / fechas / confirmacion
    "dni": None,
    "categoria": None,
    "fecha_inicio": None,
    "dias_solicitados": None,
}

# POSIBLE FUNCION PARA CORTAR EL FLUJO Y SALIR. MODIFICAR


def procesar_mensaje(texto, estado):
    if texto.strip().lower() in ["salir", "cancelar", "exit"]:
        estado["etapa"] = "inicio"  # resetea la máquina de estados
        return "Proceso cancelado. Hasta luego. Escribí 'hola' para empezar de nuevo."

    # recién acá procesás el flujo normal según la etapa
    if estado["etapa"] == "menu":
        ...
