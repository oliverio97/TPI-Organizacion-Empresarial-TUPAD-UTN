from archivos import buscar_empleado
#from solicitudes import generar_solicitud, modificar_tipo_licencia, modificar_fecha_tentativa
from validaciones import validar_dni




# MAQUINA DE ESTADOS DEL PROGRAMA
estado_usuario = {
    "etapa": "inicio",  # inicio / menu / fechas / confirmacion
    "dni": None,
    "categoria": None,
    "fecha_inicio": None,
    "dias_solicitados": None,
}
def salida(texto):
    return texto.strip().lower() in ["salir", "cancelar", "exit", "4"]
# POSIBLE FUNCION PARA CORTAR EL FLUJO Y SALIR. MODIFICAR


def procesar_mensaje(texto, estado):
    if texto.strip().lower() in ["salir", "cancelar", "exit"]:
        estado["etapa"] = "inicio"  # resetea la máquina de estados
        return "Proceso cancelado. Hasta luego. Escribí 'hola' para empezar de nuevo."

    # recién acá procesás el flujo normal según la etapa
    if estado["etapa"] == "menu":
        ...

# BLOQUE PRINCIPAL
def main():
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTIÓN DE LICENCIAS".center(50))
        print("=" * 50)
        print(
            "\nBienvenido al ChatBot de solicitudes de livencia."
            "\nEscriba 'salir en cualquier momento para cancelar.\n"
        )

#Bucle principal de la mqaquina de estados
        while True:
            match estado_usuario["etapa"]:
                case "iniciado":
                    #PEDIMOS EL DNI Y HACEMOS DOBLE VALIDACION

                    entrada = input ("Por favor, inegrese su DNI (sin puntos ni espacios):  ").strip()
                    if entrada.lower() in ["salir","cancelar", "exit", "4"]:
                        print("Proceso cancelado. ¡Hasta luego!")
                        break

                    #Vamos con la primera validacion del DNI (Digitos)
                    dni_format_valido = validar_dni(entrada)
                    if dni_format_valido: 
                        #vamos con la segunda validacion del DNI (Registros)
                        empleado = buscar_empleado(dni_format_valido)

                        if empleado: 
                            estado_usuario["dni"] = dni_format_valido
                            estado_usuario["nombre_empleado"] = empleado.get ("nombre", "Empleado")
                            print(f"\n¡Hola, {estado_usuario['nombre_empleado']}! Autenticación existosa.")

                            estado_usuario ["estapa"] = "menu_tramite"

                        else:#Si el formato es correcto pero no esta en el CSV
                            print("El DNI ingresado no se encuentra registrado en el sistema."
                                "\nPor favor, verifique el numero o cominiquese con RRHH.\n")

                    else:
                        print("DNI INVÁLIDO. Ingrese un numero de 7 u 8 digitos sin puntos ni letras.\n")

            # --- ESTADO: MENÚ DE ELECCIÓN DE TRÁMITE ---
            # Este bloque aparece inmediatamente después de que el DNI se validó con éxito
                case "menu_tramite":
                    #Menu pos-verificado del DNI

                    print("\n============== ¿QUÉ DESEA REALIZAR? ==============")
                    print("1. Iniciar una nueva solicitud de licencia")
                    print("2. Consultar el estado de una licencia")
                    print("3. Salir")
                    print("==================================================")

                    opcion_inicial = input("Su elección: ").strip()

                    if opcion_inicial.lower() in ["salir", "cancelar", "exit", "3"]:
                        print("Proceso finalizado. ¡Hasta luego!")
                        return

                    match opcion_inicial:
                        case "1":
                            print("\nPerfecto. Accediendo al sistema de solicitudes...")
                            break

                        case "2":
                            print(f"\nConsultando el estado de la licencia para el DNI ingresado...")
                            #Aca tenemos que llamar a la funcion de archivos.py
                            #solicitud = buscar_solicitud(estado_usuario["dni"])
                            #mostrar_estado(solicitud)

                        case _:
                            print("Opción no válida. Por favor, ingrese 1, 2 o 3.\n")

                case "menu_principal":
                    try:
                        print("\n=============== MENÚ PRINCIPAL ===============")
                        print("\n¿Que desea hacer?"
                            "\n1. Genera nueva solicitud"
                            "\n2. Modificar tipo de licencia"
                            "\n3. BModificar f3echa tentativa"
                            "\n4. Salir.\n"
                        )
                        print("==============================================\n")
                        menu = int(input("Su eleccion: ")).strip()
                        print()
                        if menu not in range(1, 5):
                            print(
                                "No has ingresado un numero valido. Ingresa una opcion entre 1 y 4\n"
                            )
                        else:
                            break
                    except ValueError:
                        print(
                            "No has ingresado una opcion valida. Ingresa solamente un numero entre 1 y 4.\n"
                        )

                    # estructura match- case del menu principal
                    match menu:
                        case 1:
                            ...

                        case 2:
                            ...

                        case 3:
                            ...


if __name__ == "__main__":
    main()