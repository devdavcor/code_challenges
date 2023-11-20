'''/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
'''
import random

def get_score_concept(point):
	if point == 0:
		return 'Love'
	elif point == 1:
		return '15'
	elif point == 2:
		return '30'
	elif point >= 3:
		return '40'

score = [0, 0]
winner = False
point = 0

while winner == False:
	#j = random.choice([0, 1])

	j = int(input("Ingresa el ganador del punto: "))
	score[j] += 1
	point += 1

	#print(f"Punto número {point} y ganó {j}")

	if score[0] == score[1]:
		if score[0] < 4:
			print(f"El marcador es {get_score_concept(score[0])} iguales")
		else:
			print(f"El marcador es Deuce")

	elif score[1] - score[0] != 0 :
		if (score[0] > 3 or score[1] > 3):
			if (abs(score[1] - score[0]) == 1):
				if score[0] > score[1]:
					print(f"El marcador es [Ventaja, {get_score_concept(score[1])}]")
				else:
					print(f"El marcador es [{get_score_concept(score[0])}, Ventaja]")
			elif (abs(score[1] - score[0]) >= 2):
				winner = True
				if score[0] > score[1]:
					print(f"El marcador es [Winner, {get_score_concept(score[1])}]")
				else:
					print(f"El marcador es [{get_score_concept(score[0])}, Winner]")
		else:
			print(f"El marcador es [{get_score_concept(score[0])}, {get_score_concept(score[1])}]")














# Inicié a las 10:14 pm del 19 de noviembre de 2023
# Tardé 30 minutos en resolverlo