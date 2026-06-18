from archivos import buscar_empleado, consultar_saldo_dias
from validaciones import validar_dni
from solicitudes import generar_solicitud

# MAQUINA DE ESTADOS: Diccionario con la "memoria" de la sesión
estado_usuario = {
    "etapa": "inicio",
    "dni": None,
    "nombre_empleado": None,
    "categoria": None,
    "descripcion_solicitud": None,
    "fecha_inicio": None,
    "dias_disponibles": None,
    "dias_solicitados": None,
}

# =========================================================
# FUNCIONES MANEJADORAS DE ESTADOS
# =========================================================


def manejar_inicio():
    """Maneja el estado inicial: Autenticación del usuario"""
    entrada = input("Por favor, ingrese su DNI (sin puntos ni espacios): ").strip()

    if entrada.lower() in ["salir", "cancelar", "exit"]:
        print("Proceso cancelado. ¡Hasta luego!")
        return False  # Detiene el programa

    dni_format_valido = validar_dni(entrada)
    if dni_format_valido:
        empleado = buscar_empleado(dni_format_valido)
        if empleado:
            estado_usuario["dni"] = dni_format_valido
            estado_usuario["nombre_empleado"] = empleado.get("nombre", "Empleado")
            print(
                f"\n¡Hola, {estado_usuario['nombre_empleado']}! Autenticación exitosa."
            )

            # TRANSICIÓN DE ESTADO
            estado_usuario["etapa"] = "menu_tramite"
        else:
            print("El DNI ingresado no se encuentra registrado. Verifique el número.\n")
    else:
        print("DNI INVÁLIDO. Ingrese un numero de 7 u 8 digitos sin puntos.\n")

    return True


def manejar_menu_tramite():
    """Maneja el menú de selección inicial de la gestión"""
    print("\n============== ¿QUÉ DESEA REALIZAR? ==============")
    print("1. Iniciar una nueva solicitud de licencia")
    print("2. Consultar el estado de una licencia")
    print("3. Salir")
    print("==================================================")

    opcion = input("Su elección: ").strip()

    match opcion:
        case "1":
            print("\nPerfecto. Accediendo al menú de solicitudes...")
            estado_usuario["etapa"] = "menu_principal"  # Transición
        case "2":
            print(
                f"\nConsultando estado para el DNI {estado_usuario['dni']}... (En desarrollo)"
            )
        case "3" | "salir" | "cancelar":
            print("Proceso finalizado. ¡Hasta luego!")
            return False
        case _:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.\n")

    return True


def manejar_menu_principal():
    """Maneja el menú principal de licencias"""
    try:
        print("\n=============== TIPO DE TRÁMITE ===============")
        print("1. Generar nueva solicitud")
        print("2. Modificar tipo de licencia")
        print("3. Modificar fecha tentativa")
        print("4. Volver al menú anterior")
        print("==============================================\n")

        opcion = int(input("Su eleccion: ").strip())

        match opcion:
            case 1:
                print("Iniciando generación de solicitud...")
                nuevo_estado = tipo_solicitud(estado_usuario["dni"])
                estado_usuario["etapa"] = nuevo_estado  ## CHEQUEAR ESTO
                # estado_usuario["etapa"] = "pidiendo_fechas" # ESTA ES OTRA OPCION
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

    return True


def tipo_solicitud(dni):
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

            case 1:  # VACACIONES
                print("Iniciando generación de solicitud...")
                if consultar_saldo_dias(dni):
                    print(
                        f"{estado_usuario["nombre_empleado"]} tenes {consultar_saldo_dias(dni)} dias disponibles"
                    )
                    return "solicitar_dias"
                else:
                    print(
                        f" {estado_usuario["nombre_empleado"]}, no tenes dias disponibles. Para mas informacion, contactate con RRHH."
                    )
                    return "salir"

            case 2:  # DIAS PERSONALES
                print("Iniciando generación de solicitud...")
                if consultar_saldo_dias(dni):
                    print(
                        f"{estado_usuario["nombre_empleado"]}, tenes {consultar_saldo_dias(dni)} dias disponibles"
                    )
                    return "solicitar_dias"
                else:
                    print(
                        f" {estado_usuario["nombre_empleado"]}, no tenes dias disponibles. Para mas informacion, contactate con RRHH."
                    )
                    return "salir"

            case 3:  # LICENCIA POR ENFERMEDAD / OTRO TIPO DE LICENCIA
                print("Iniciando generación de solicitud...")
                print(
                    f"{estado_usuario["nombre_empleado"]}, por favor ingresá la descripcion del justificativo por el cual necesitás tomarte dias de licencia. \nRecordá que, de ser necesario, un miembro de RRHH podra contactarse con vos para solicitarte documentación adicional. \n"
                )
                justificativo = input("Descripcion del justificativo: ")
                estado_usuario["descripcion_solicitud"] = justificativo
                return "solicitar_dias"

            case 4:
                return "menu_tramite"  # Transición hacia atrás
            case _:
                print("No has ingresado un numero valido entre 1 y 4.\n")

    except ValueError:
        print("Error: Ingresa solamente un numero entero.\n")


# =========================================================
# ENRUTADOR PRINCIPAL
# =========================================================


def procesar_estado_actual():
    """
    Evalúa en qué etapa está el usuario y delega la ejecución
    a la función manejadora correspondiente.
    """
    match estado_usuario["etapa"]:
        case "inicio":
            return manejar_inicio()

        case "menu_tramite":
            return manejar_menu_tramite()

        case "menu_principal":
            return manejar_menu_principal()

        case "salir":
            return

        case _:
            # Fallback de seguridad por si el estado se rompe
            print("Error: Estado desconocido. Volviendo al inicio...")
            estado_usuario["etapa"] = "inicio"
            return True
