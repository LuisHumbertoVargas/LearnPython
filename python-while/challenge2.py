import random;

num_aleatorio = random.randint(1,10);

num_input = 0
contador = 1

while num_input != num_aleatorio:
    print('Adivina un número entre 1 y 10: ')
    num_input = input(f'Intento No. {contador}: ')

    if num_input.strip() == '':
        continue

    if num_input.isnumeric() == False:
        contador += 1
        print('¡Ingrese un valor númerico, por favor!\n')
        continue

    if int(num_input) != num_aleatorio:
        contador += 1
        if int(num_input) < num_aleatorio:
            print('Tu número es demasiado bajo, ¡inténtalo de nuevo!\n')

        if int(num_input) > num_aleatorio:
            print('Tu número es demasiado alto, ¡inténtalo de nuevo!\n')

        continue

    if int(num_input) == num_aleatorio:
        print("\n¡ADIVINASTE!")
        break

print(f'Has adivinado en {contador} intentos')

    



