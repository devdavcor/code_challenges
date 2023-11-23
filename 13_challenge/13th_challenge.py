'''
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
'''

import calendar


def obtener_dia_semana(año, mes):
	_, últimos_días = calendar.monthrange(año, mes)
	días_del_mes = [f"{año}-{mes:02d}-{día:02d}" for día in range(1, últimos_días + 1)]

	for día in días_del_mes:
		fecha = datetime.datetime.strptime(día, "%Y-%m-%d")
		día_semana = calendar.day_name[fecha.weekday()]
		print(f"{día}: {día_semana}")


# Asegúrate de importar datetime al principio de tu código
import datetime

# Ejemplo de uso
año = 2023
mes = 11
obtener_dia_semana(año, mes)
