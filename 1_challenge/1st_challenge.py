'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for i in range(101):
	if (i % 3 == 0) and (i % 5 == 0):
		print(f"{i} -> fizzbuzz")
	elif (i % 3 == 0):
		print(f"{i} -> fizz")
	elif (i % 5 == 0):
		print(f"{i} -> buzz")
	elif i > 0:
		print(f"{i}")

# Inicié a las 9:25 pm del 19 de noviembre de 2023
# Tardé 6 minutos en resolverlo
