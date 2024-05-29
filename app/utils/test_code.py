'''from datetime import datetime

def validar_fecha_creacion_y_expiracion(fecha_creacion, fecha_expiracion):
    formato = "%Y-%m-%d %H:%M:%S"  # Eliminar .%f para manejar microsegundos

    # Convertir las cadenas de fecha en objetos datetime
    fecha_creacion_dt = datetime.strptime(fecha_creacion, formato)
    fecha_expiracion_dt = datetime.strptime(fecha_expiracion, formato)

    # Comparar las fechas
    if fecha_creacion_dt < fecha_expiracion_dt:
        print("La fecha de creación es anterior a la fecha de expiración.")
        return True
    else:
        print("La fecha de creación es posterior o igual a la fecha de expiración.")
        return False

# Ejemplo de uso
fecha_creacion = "2024-04-22 21:32:36"
fecha_expiracion = "2024-05-22 21:32:36"
if __name__ == '__main__':
    validar_fecha_creacion_y_expiracion(fecha_creacion, fecha_expiracion)'''

'''fecha_con_microsegundos = "2024-05-22T21:32:36.538489"
fecha_sin_microsegundos = fecha_con_microsegundos.split('.')[0]
if __name__ == '__main__':
    print(fecha_sin_microsegundos)'''
from datetime import datetime

def comparar_fechas_y_calcular_dias_restantes(fecha_string):
    # Convertir la cadena de fecha en un objeto datetime
    fecha_proporcionada = datetime.strptime(fecha_string, "%Y-%m-%d")

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()
    
    # Calcular los días restantes
    dias_restantes = (fecha_proporcionada - fecha_actual).days
    print("Días restantes:", dias_restantes)
    
    
    # Comparar las fechas
    if fecha_proporcionada > fecha_actual:
        print(f"La fecha proporcionada es posterior a la fecha y hora actual y faltan {dias_restantes} días.")
    elif fecha_proporcionada < fecha_actual:
        dias_caducado = abs(dias_restantes)
        print(f"Tu membresía expiró el {fecha_proporcionada} hace {dias_caducado} dias.")
    else:
        print("Tu membresía caduca hoy.")

if __name__ == '__main__':
    fecha_proporcionada = "2024-02-22"
    comparar_fechas_y_calcular_dias_restantes(fecha_proporcionada)
