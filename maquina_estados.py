from archivos import buscar_empleado, consultar_saldo_dias, recuperar_sesion
from validaciones import validar_dni, validar_fecha, entrada_segura
from solicitudes import generar_solicitud

# MAQUINA DE ESTADOS: Diccionario con la "memoria" de la sesión
estado_usuario = {
    "etapa": "inicio",
    "dni": None,
    "nombre_empleado": None,
    "apellido_empleado": None,
    "categoria": None,
    "descripcion_solicitud": None,
    "dias_disponibles": None,
    "dias_solicitados": None,
    "fecha_inicio": None,
}

# =========================================================
# FUNCIONES MANEJADORAS DE ESTADOS
# =========================================================


def manejar_inicio():
    """Maneja el estado inicial: Autenticación del usuario"""
    entrada = entrada_segura(
        "Por favor, ingrese su DNI (sin puntos ni espacios): "
    ).strip()

    dni_format_valido = validar_dni(entrada)
    if dni_format_valido:
        empleado = buscar_empleado(dni_format_valido)
        if empleado:
            estado_usuario["dni"] = dni_format_valido
            estado_usuario["nombre_empleado"] = empleado.get("nombre", "Empleado")
            estado_usuario["apellido_empleado"] = empleado.get("apellido", "Empleado")
            print(
                f"\n¡Hola, {estado_usuario['nombre_empleado']}! Autenticación exitosa."
            )
            sesion_guardada = recuperar_sesion(dni_format_valido)
            if sesion_guardada:
                respuesta = (
                    input(
                        "Tienes un trámite sin terminar. ¿Deseas retomarlo? (si/no): "
                    )
                    .strip()
                    .lower()
                )
                if respuesta in ["si", "s", "sí"]:
                    # Pisamos el estado actual vacío con los datos que trajimos del CSV
                    estado_usuario.update(sesion_guardada)
                    print(f"Retomando desde la etapa: {estado_usuario['etapa']}...")
                    return True  # Sale de la función y el enrutador salta a esa etapa
            # -------------------------------------

            # Si no tenía sesión o eligió no retomarla, arranca desde cero
            estado_usuario["dni"] = dni_format_valido
            estado_usuario["nombre_empleado"] = empleado.get("nombre", "Empleado")
            estado_usuario["etapa"] = "menu_tramite"

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

    opcion = entrada_segura("Su elección: ").strip()

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
        print("===============================================\n")

        opcion = int(entrada_segura("Su eleccion: ").strip())

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
        print("=================================================\n")

        opcion = int(entrada_segura("Su eleccion: ").strip())
        match opcion:

            case 1:  # VACACIONES
                print("Iniciando generación de solicitud...")
                if consultar_saldo_dias(dni):
                    print(
                        "\n=============== TIPO DE SOLICITUD: VACACIONES ==============="
                    )
                    print(
                        f"{estado_usuario["nombre_empleado"]}, tenes {consultar_saldo_dias(dni)} dias disponibles"
                    )
                    print(
                        "=============================================================\n"
                    )
                    estado_usuario["categoria"] = "vacaciones"
                    estado_usuario["dias_disponibles"] = consultar_saldo_dias(dni)
                    return "solicitar_dias"
                else:
                    print(
                        f" {estado_usuario["nombre_empleado"]}, no tenes dias disponibles. Para mas informacion, contactate con RRHH."
                    )
                    print("==============================================\n")
                    return "salir"

            case 2:  # DIAS PERSONALES
                print("Iniciando generación de solicitud...")
                print(
                    "\n=============== TIPO DE SOLICITUD: DIAS PERSONALES ==============="
                )
                if consultar_saldo_dias(dni):
                    print(
                        f"{estado_usuario["nombre_empleado"]}, tenes {consultar_saldo_dias(dni)} dias disponibles"
                    )
                    print("==============================================\n")
                    estado_usuario["categoria"] = "dias_personales"
                    estado_usuario["dias_disponibles"] = consultar_saldo_dias(dni)
                    return "solicitar_dias"
                else:
                    print(
                        f" {estado_usuario["nombre_empleado"]}, no tenes dias disponibles. Para mas informacion, contactate con RRHH."
                    )
                    print("==============================================\n")
                    return "salir"

            case 3:  # LICENCIA POR ENFERMEDAD / OTRO TIPO DE LICENCIA
                print("Iniciando generación de solicitud...")
                print("\n=============== TIPO DE SOLICITUD: LICENCIAS ===============")
                print(
                    f"{estado_usuario["nombre_empleado"]}, por favor ingresá la descripcion del justificativo por el cual necesitás tomarte dias de licencia. \nRecordá que, de ser necesario, un miembro de RRHH podra contactarse con vos para solicitarte documentación adicional. \n"
                )
                print("==============================================\n")
                justificativo = entrada_segura("Descripcion del justificativo: ")
                estado_usuario["categoria"] = "licencia"
                estado_usuario["descripcion_solicitud"] = justificativo
                return "solicitar_dias"

            case 4:
                return "menu_tramite"  # Transición hacia atrás
            case _:
                print("No has ingresado un numero valido entre 1 y 4.\n")

    except ValueError:
        print("Error: Ingresa solamente un numero entero.\n")


def solicitar_dias():
    print("¿Cuantos días deseas tomarte?")
    try:
        dias_usuario = int(entrada_segura("Tu eleccion: "))
        if not estado_usuario["categoria"] == "licencia":
            if dias_usuario > estado_usuario["dias_disponibles"]:
                print(
                    f"No tenes días suficientes. Recordá que tenes {estado_usuario['dias_disponibles']} dias disponibles. "
                )
                estado_usuario["etapa"] = "menu_tramite"
                return True
            else:
                estado_usuario["dias_solicitados"] = dias_usuario
                estado_usuario["etapa"] = "validar_fechas"
                return True
        estado_usuario["dias_solicitados"] = dias_usuario
        estado_usuario["etapa"] = "validar_fechas"
        return True

    except ValueError:
        print(
            "No has ingresado una opcion valida. Ingresa un numero entero para solicitar dias de licencia. \n"
        )
        estado_usuario["etapa"] = "menu_tramite"
        return True


def solicitar_fechas():
    print("\n=============== INGRESO FECHA INICIO ===============")
    print(
        "Ingresa la fecha de inicio de tus dias solicitados de licencia.\nRecorda que estos días se tomarán de corrido teniendo en cuenta el dia de inicio y la cantidad de días solicitados.\n"
        "Para ingresar la fecha, utiliza el formato DD/MM/YYYY \n(dos digitos para el dia, dos digitos para el mes, cuatro digitos para el año) separados por la barra (/). "
    )
    print("===================================================\n")
    dia_inicio = validar_fecha(entrada_segura("Tu eleccion: "))
    if dia_inicio is None:
        print("Has ingresado un formato incorrecto para la fecha. \n")
        return True
    elif dia_inicio is False:
        print(
            "La fecha ingresada no es correcta. Debes ingresar una fecha como mínimo 15 días hábiles posteriores a la fecha de hoy. \n"
        )
        return True
    else:
        estado_usuario["fecha_inicio"] = dia_inicio
        print(f"La fecha es correcta? {dia_inicio}\n")
        chequeo_fecha = entrada_segura(f'Ingresa "si" o "no":')
        if chequeo_fecha == "no":
            print()
            return True
        elif chequeo_fecha == "si":
            estado_usuario["etapa"] = "resumen"
            return True
        else:
            print("No ingresaste una opcion valida.")
            return True


def mostrar_resumen():
    print(
        "Por favor, leé atentamente el resumen de tu solicitud antes de confirmar. \n"
    )
    print("\n=============== RESUMEN SOLICITUD ===============\n")
    print(f"- DNI solicitante: {estado_usuario['dni']}.")
    print(
        f"- Nombre y apellido solicitante: {estado_usuario['nombre_empleado']} {estado_usuario["apellido_empleado"]}"
    )
    print(f"- Tipo de licencia solicitada: {estado_usuario['categoria']}")
    print(f"- Días solicitados: {estado_usuario['dias_solicitados']}")
    print(f"- Fecha de inicio de la licencia: {estado_usuario['fecha_inicio']}")
    if estado_usuario["categoria"] == "licencia":
        print(f"- Justificativo ingresado: {estado_usuario["descripcion_solicitud"]}")
    print("\n==============================================\n")
    print()
    print("¿Los datos son correctos?")
    chequeo_resumen = entrada_segura(f'Ingresa "si" o "no":')
    if chequeo_resumen == "no":
        print("\nOk, proceso cancelado. Volviendo al menú principal.\n")
        estado_usuario["etapa"] = "inicio"
        return True
    elif chequeo_resumen == "si":
        estado_usuario["etapa"] = "finalizacion"
        return True
    else:
        print("No ingresaste una opcion valida.")
        return True


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

        case "solicitar_dias":
            return solicitar_dias()

        case "validar_fechas":
            return solicitar_fechas()

        case "resumen":
            return mostrar_resumen()

        case "finalizacion":
            generar_solicitud(estado_usuario)
            print(
                "Se ha guardado tu solicitud con éxito. En los proximos días se contactarán con vos para informar los proximos pasos."
            )
            return

        case "salir":
            return

        case _:
            # Fallback de seguridad por si el estado se rompe
            print("Error: Estado desconocido. Volviendo al inicio...")
            estado_usuario["etapa"] = "inicio"
            return True
