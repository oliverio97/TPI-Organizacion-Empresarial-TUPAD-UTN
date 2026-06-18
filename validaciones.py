from datetime import datetime, timedelta
import sys  # Importación necesaria para poder apagar el programa

# validaciones.py
import sys
from archivos import guardar_sesion


# IMPORTANTE: Para evitar el error de "importación circular" del que hablamos antes,
# la importación del estado la hacemos DENTRO de la función, justo antes de usarla.
def entrada_segura(mensaje_prompt):
    entrada = input(mensaje_prompt).strip()

    if entrada.lower() in ["salir", "cancelar", "exit"]:
        # Importamos la memoria en el instante que la necesitamos
        from maquina_estados import estado_usuario

        # Solo guardamos si el usuario ya se había logueado (tiene DNI)
        if estado_usuario.get("dni"):
            guardar_sesion(estado_usuario)
            print("\nProgreso guardado. Podrás retomarlo cuando vuelvas.")

        print("\nProceso cancelado por el usuario. ¡Hasta luego!")
        sys.exit()

    return entrada


# Valida que el DNI sea numérico y tenga una longitud lógica (7 u 8 dígitos).
# Devuelve el DNI como entero si es válido, o None si no lo es.
def validar_dni(dni_texto):
    dni_texto = dni_texto.strip()
    if dni_texto.isdigit() and 7 <= len(dni_texto) <= 8:
        return int(dni_texto)
    return None


def validar_fecha(entrada):
    entrada = entrada.strip()
    try:
        # CORRECCIÓN: strptime convierte el texto (string) en un objeto de fecha
        fecha = datetime.strptime(entrada, "%d/%m/%Y")
    except ValueError:
        # Si el usuario ingresa texto o un formato incorrecto (ej: 2026/05/10)
        return None

    hoy = datetime.today()
    dias_habiles = 0
    fecha_minima = hoy

    # Cálculo de los 15 días hábiles en el futuro
    while dias_habiles < 15:
        fecha_minima += timedelta(days=1)
        if fecha_minima.weekday() < 5:  # 0 a 4 corresponden de Lunes a Viernes
            dias_habiles += 1

    # Verificación contra la fecha ingresada
    if fecha < fecha_minima:
        return False

    return entrada  # Retorna la fecha original en texto si pasó todas las pruebas


def validar_dias(
    entrada,
):  # Devuelve los dias como enteros si son validos, o none si el usuario ingreso letras, cero o un numero negativo.
    entrada = entrada.strip()
    if not entrada.isdigit():
        return None
    dias = int(entrada)
    if dias <= 0:
        return None
    return dias


def tipo_descripcion(
    entrada,
):  # si el usuario ingresa menos de 10 caracteres devuelve None, si no devuelve el texto limpio.
    entrada = entrada.strip()
    if len(entrada) < 10:
        return None
    return entrada
