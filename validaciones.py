
#Valida que el DNI sea numérico y tenga una longitud lógica (7 u 8 dígitos). 
#Devuelve el DNI como entero si es válido, o None si no lo es.
def validar_dni(dni_texto):
    dni_texto = dni_texto.strip()
    if dni_texto.isdigit() and 7 <= len(dni_texto) <=8:
        return int(dni_texto)
    return None

def validar_fecha():
    pass

def validar_dias():
    pass

def tipo_descripcion():
    pass


