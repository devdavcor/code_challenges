'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

def is_pair (number):
	if number % 2 == 0:
		return 'SÍ es par'
	else:
		return 'NO es par'

def is_fibonacci (number):
	a = 1
	b = 0
	condition = False
	while condition == False:
		aux = a + b
		b = a
		a = aux
		if a > number:
			return 'NO pertenece a Fibonacci'
		elif a == number:
			return 'SÍ pertenece a Fibonacci'

a = 1
b = 0

number = int(input("Ingresa un número para validar: "))

number_2="{:,.2f}".format(number)

print(f"El número {number_2} {is_pair (number)} y {is_fibonacci (number)}")

# Inicié a las 12:20 horas del 20 de noviembre de 2023
# Tardé 13 minutos en resolverlo
