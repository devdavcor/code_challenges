'''
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
'''

import calendar
import datetime

def get_weekday(year, month):

    _, last_days = calendar.monthrange(year, month)
    days_of_month = [f"{year}-{month:02d}-{day:02d}" for day in range(1, last_days + 1)]

    for day in days_of_month:
        date = datetime.datetime.strptime(day, "%Y-%m-%d")
        weekday = calendar.day_name[date.weekday()]
        if day[8:] == '13' and weekday == 'Friday':
            print(f"{day}: is {weekday} 13th")

# Ejemplo de uso
year = 2023
month = 1
for j in range (2000, 2025):
	for i in range (12):
		get_weekday(j, i+1)

