from maquina_estados import estado_usuario


# Flujo 1: Generar solicitud
def generar_solicitud():
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
                consultar_saldo_Dias(dias)
                print("Iniciando generación de solicitud...")

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
