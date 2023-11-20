'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *//*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

cadena = input ("Ingresan un texto: ")
print(cadena)

resultado = "La nueva cadena es: \n"
for letra in cadena:
	if (letra == 'A') or (letra == 'a'):
		resultado = resultado + ' 4 '
	elif (letra == 'B') or (letra == 'b'):
		resultado = resultado + ' I3 '
	elif (letra == 'C') or (letra == 'c'):
		resultado = resultado + ' [ '
	elif (letra == 'D') or (letra == 'd'):
		resultado = resultado + ' ) '
	elif (letra == 'E') or (letra == 'e'):
		resultado = resultado + ' 3 '
	elif (letra == 'F') or (letra == 'f'):
		resultado = resultado + ' |= '
	elif (letra == 'G') or (letra == 'g'):
		resultado = resultado + ' & '
	elif (letra == 'H') or (letra == 'h'):
		resultado = resultado + ' # '
	elif (letra == 'I') or (letra == 'i'):
		resultado = resultado + ' 1 '
	elif (letra == 'J') or (letra == 'j'):
		resultado = resultado + ' ,_| '
	elif (letra == 'K') or (letra == ' k '):
		resultado = resultado + ' >| '
	elif (letra == 'L') or (letra == ' l '):
		resultado = resultado + ' 1 '
	elif (letra == 'M') or (letra == 'm'):
		resultado = resultado + " /\/| "
	elif (letra == 'N') or (letra == 'n'):
		resultado = resultado + ' ^/ '
	elif (letra == 'Ñ') or (letra == 'ñ'):
		resultado = resultado + ' ^´´/ '
	elif (letra == 'O') or (letra == ' o '):
		resultado = resultado + ' 0 '
	elif (letra == 'P') or (letra == 'p'):
		resultado = resultado + ' |* '
	elif (letra == 'Q') or (letra == 'q'):
		resultado = resultado + ' (_,) '
	elif (letra == 'R') or (letra == 'r'):
		resultado = resultado + ' I2 '
	elif (letra == 'S') or (letra == 's'):
		resultado = resultado + ' 5 '
	elif (letra == 'T') or (letra == 't'):
		resultado = resultado + ' 7 '
	elif (letra == 'U') or (letra == 'u'):
		resultado = resultado + ' (_) '
	elif (letra == 'V') or (letra == 'v'):
		resultado = resultado + ' \/ '
	elif (letra == 'W') or (letra == 'w'):
		resultado = resultado + ' \/\/ '
	elif (letra == 'X') or (letra == 'x'):
		resultado = resultado + ' >< '
	elif (letra == 'Y') or (letra == 'y'):
		resultado = resultado + ' j '
	elif (letra == 'Z') or (letra == 'z'):
		resultado = resultado + ' 2 '

print(resultado)

# Inicié a las 9:40 pm del 19 de noviembre de 2023
# Tardé 23 minutos en resolverlo


