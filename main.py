#from archivos import inicializar_csv
#from solicitudes import generar_solicitud, modificar_tipo_licencia, modificar_fecha_tentativa





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
    while True:  # aca poner el menu con sus validaciones
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTIÓN DE LICENCIAS".center(50))
        print("=" * 50)

        print(
            "\nBienvenido al ChatBot de solicitudes de livencia."
            "\nEscriba 'salir en cualquier momento para cancelar.\n"
        )
        while True:  # validacion de errores en las opciones del menu
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
                        "No has ingresado un numero valido. Ingresa una opcion entre 1 y 7\n"
                    )
                else:
                    break
            except ValueError:
                print(
                    "No has ingresado una opcion valida. Ingresa solamente un numero entre 1 y 7.\n"
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