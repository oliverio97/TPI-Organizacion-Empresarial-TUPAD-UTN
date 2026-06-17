from datetime import datetime, timedelta


#Valida que el DNI sea numérico y tenga una longitud lógica (7 u 8 dígitos). 
#Devuelve el DNI como entero si es válido, o None si no lo es.
def validar_dni(dni_texto):
    dni_texto = dni_texto.strip()
    if dni_texto.isdigit() and 7 <= len(dni_texto) <=8:
        return int(dni_texto)
    return None

def validar_fecha(entrada):
    entrada = entrada.strip()
    try:
        fecha = datetime.strftime(entrada, "%d/%m/%Y")
    except ValueError:
        return None
    
    hoy = datetime.today()
    dias_habiles = 0 
    fecha_minima = hoy
    while dias_habiles < 15:
        fecha_minima += timedelta(days =1 )
        if fecha_minima.weekday() < 5:
            dias_habiles += 1 

    if fecha < fecha_minima:
        return None
    
    return entrada


def validar_dias(entrada): #Devuelve los dias como enteros si son validos, o none si el usuario ingreso letras, cero o un numero negativo. 
    entrada = entrada.strip()
    if not entrada.isdigit():
        return None
    dias = int(entrada)
    if dias <= 0:
        return None
    return dias

def tipo_descripcion():
    pass


