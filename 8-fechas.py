#luz Atamari
# Fechas en Python

from datetime import date, datetime

# fecha actual
hoy = date.today()
print(hoy)

# formatear fecha
formateado = hoy.strftime("%d/%m/%Y")
print(formateado)

# Hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#capturar el año
anio = fecha_actual.year
print(anio)

mes = fecha_actual.month
print(mes)

dia = fecha_actual.day
print(dia)

hora_actual = fecha_actual.strftime("%H:%M:%S")
print( hora_actual)

# formato AM PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %P")
print(hora_am_pm)
