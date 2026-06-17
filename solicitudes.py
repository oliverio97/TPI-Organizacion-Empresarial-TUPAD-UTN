from archivos import consultar_saldo_dias


# Flujo 1: Generar solicitud
def generar_solicitud(dni):
    """Maneja la generacion de licencias"""
    try:
        print("\n=============== TIPO DE SOLICITUD ===============")
        print("1. Vacaciones")
        print("2. Tomarse días personales")
        print("3. Licencia por enfermedad / maternidad / otros tipos de licencia. ")
        print("4. Volver al menú anterior")
        print("==============================================\n")

        opcion = int(input("Su eleccion: ").strip())

        match opcion:
            case 1:
                print("Iniciando generación de solicitud...")
                dias_disponibles = consultar_saldo_dias(dni)
                if int(dias_disponibles) > 0:
                    print(f"Tenes {dias_disponibles} dias disponibles.")
                else:
                    return None

            case 2:
                print("Opción en desarrollo...")
            case 3:
                print("Opción en desarrollo...")
            case 4:
                estado_usuario["etapa"] = "menu_tramite"  # Transición hacia atrás
            case _:
                print("No has ingresado un numero valido entre 1 y 4.\n")

    except ValueError:
        print("Error: Ingresa solamente un numero entero.\n")


# Flujo 2: Modificar tipo de licencia
def modificar_tipo_licencia():
    pass


# Flujo 3: Modificar fecha tentativa
def modificar_fecha_tentativa():
    pass
