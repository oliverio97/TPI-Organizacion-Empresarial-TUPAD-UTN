
#Valida que el DNI sea numérico y tenga una longitud lógica (7 u 8 dígitos). 
#Devuelve el DNI como entero si es válido, o None si no lo es.
def validar_dni(dni_texto):
    dni_texto = dni_texto.strip()
    if dni_texto.isdigit() and 7 <= len(dni_texto) <=8:
        return int(dni_texto)
    return None

def validar_fecha():
    pass

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


