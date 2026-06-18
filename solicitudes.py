from validaciones import es_salida


## EN ESTE MODULO PONEMOS SOLAMENTE LAS FUNCIONES PARA EMPAQUETAR Y ENVIAR LA SOLICITUD COMPLETA
# Flujo 1: Generar solicitud
def generar_solicitud():
    pass


def manejar_pidiendo_dias():
    """Estado: Pide la cantidad de días y valida contra el saldo disponible"""
    print(f"\nTienes {estado_usuario['dias_disponibles']} días disponibles.")
    entrada = input("¿Cuántos días te querés tomar? (o escribe 'cancelar'): ").strip()

    if entrada.lower() in ["cancelar", "salir"]:
        print("Operación cancelada. Volviendo al menú...")
        estado_usuario["etapa"] = "menu_principal"
        return True

    try:
        dias_pedidos = int(entrada)

        # VALIDACIONES (Camino Infeliz)
        if dias_pedidos <= 0:
            print("Error: Debes ingresar un número mayor a 0.\n")
            # No cambiamos de etapa, el bucle volverá a ejecutar esta función

        elif dias_pedidos > estado_usuario["dias_disponibles"]:
            print(
                f"Error: No puedes pedir {dias_pedidos} días. Solo tienes {estado_usuario['dias_disponibles']} disponibles.\n"
            )
            # Se queda en el mismo estado para volver a intentar

        else:
            # CAMINO FELIZ
            estado_usuario["dias_solicitados"] = dias_pedidos
            print(f"Perfecto, has solicitado {dias_pedidos} días.")

            # AVANCE DE ESTADO
            estado_usuario["etapa"] = "pidiendo_fechas"

    except ValueError:
        print("Error: Por favor, ingresa solo números enteros.\n")

    return True


# Flujo 2: Modificar tipo de licencia
def modificar_tipo_licencia():
    pass


# Flujo 3: Modificar fecha tentativa
def modificar_fecha_tentativa():
    pass
