import random

# Creo mis listas para formar mi baraja por medio de ciclos for
palo = ['Corazones', 'Picas', 'Treboles', 'Diamantes']
rango = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'As']
baraja = []

# Recorro primero la lista de palos para elegir mi figura
for figura in palo:
    # Recorro la lista de rango para elegir los valores para dicha figura
    for valor in rango:
        # Agrego a mi lista "bajara[]" los elementos combinados para formar mis cartas
        baraja.append(f'{valor} de {figura}')
# print(baraja)
# Calculo la longitud de mi baraja
total_cartas = len(baraja)
# Imprimo el total de cartas que hay en mi baraja
print(f'Hay un total de {total_cartas} cartas en la baraja')

# Elijo 5 cartas de la baraja al azar para repartir a mi jugador
print('Repartiendo...')
jugador1 = random.choices(baraja, k=5)
# Recorro la lista de cartas que le tocó a mi jugador para removerlas de la baraja
for mano in jugador1:
    baraja.remove(mano)
# Imprimo el nuevo total de cartas que existen en mi baraja después de hacer el reparto
print('Hay un total de '+ str(len(baraja))+ ' cartas en la baraja')
# Imprimo la mano que le toco a mi jugador
print('Cartas del Jugador1:')
print(jugador1)

print('Baraja después del reparto: ')
# Ya no existen esas cartas en mi baraja actualizada
for cartas in baraja:
    print(cartas)



