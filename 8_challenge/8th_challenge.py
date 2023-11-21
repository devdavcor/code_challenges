import time

def gen_random_int():
    aux = str(time.time())
    return str(aux[-1]) + str(aux[-2])

# Ejemplo de uso
rand_number = gen_random_int()

print("Número aleatorio:", rand_number)

# Inicié a las 00:15 horas del 21 de noviembre de 2023
# Tardé 7 minutos en resolverlo