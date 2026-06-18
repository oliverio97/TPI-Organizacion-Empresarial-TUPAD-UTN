from archivos import buscar_empleado

# from solicitudes import generar_solicitud, modificar_tipo_licencia, modificar_fecha_tentativa
from validaciones import validar_dni
from maquina_estados import procesar_estado_actual


def main():
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN DE LICENCIAS".center(50))
    print("=" * 50)
    print("Bienvenido al ChatBot de solicitudes de licencia.")
    print("Escribí 'salir' en cualquier momento para cancelar.\n")

    # Bucle principal del programa
    ejecutando = True
    while ejecutando:
        # Llamamos a la función del módulo maquina_estados.
        # Nos devolverá True para que el while siga, o False si el usuario eligió salir.
        ejecutando = procesar_estado_actual()
        if not ejecutando:
            break


if __name__ == "__main__":
    main()
