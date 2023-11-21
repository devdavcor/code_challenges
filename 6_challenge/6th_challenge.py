'''/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */'''

# A -> 🗿 -> Piedra gana a: C, D
# B -> 📄 -> Papel gana a:
# C -> ✂️ -> Tijera
# D -> 🦎 -> Lagarto
# E -> 🖖 -> Spock

def game_result(player_1, player_2):
	elements = ['A', 'B', 'C', 'D', 'E']
	wins_against = [['D', 'C'], ['A', 'E'], ['B', 'D'], ['E', 'B'], ['A', 'C']]
	#wins_against = [['E', 'B'], ['D', 'C'], ['A', 'E'], ['A', 'C'], ['A', 'D']]
	if player_1 == player_2:
		print(f"El juego es un empate de {emoji_print(player_1)}")
		return 3
	elif player_2 in wins_against[elements.index(player_1)]:
		print(f"{emoji_print(player_1)} gana a {emoji_print(player_2)}")
		return 2
	else:
		print(f"{emoji_print(player_2)} gana a {emoji_print(player_1)}")
		return 1

def emoji_print(element):
	if element == 'A':
		return '🗿'
	elif element == 'B':
		return '📄'
	elif element == 'C':
		return '✂️'
	elif element == 'D':
		return '🦎'
	elif element == 'E':
		return '🖖'

while True:
	player_1 = input("Ingrese una letra: ").upper()
	if player_1 in ['A', 'B', 'C', 'D', 'E']:
		break
	else:
		print("Por favor, ingrese una letra válida ('A', 'B', 'C', 'D', 'E').")

while True:
	player_2 = input("Ingrese una letra: ").upper()
	if player_2 in ['A', 'B', 'C', 'D', 'E']:
		break
	else:
		print("Por favor, ingrese una letra válida ('A', 'B', 'C', 'D', 'E').")

game_result(player_1, player_2)

# Inicié a las 11:00 pm del 20 de noviembre de 2023
# Tardé 30 minutos en resolverlo



