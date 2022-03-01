import random;

num_aleatorio = random.randint(1,5);

num_input = 0
contador = 1

while num_input != num_aleatorio:
    num_input = input('Adivina un número entre 1 al 5: ');

    if num_input.strip() == '':
        continue

    if num_input.isnumeric() == False:
        contador += 1
        # print('Ingresa un valor numérico')
        continue

    if int(num_input) != num_aleatorio:
        print('No adivinaste, ingresa otro número:\n')
        contador += 1
        continue

    # if int(num_input) == num_aleatorio:
    #     print("¡ADIVINASTE!")
    #     break

    else: 
        print("¡ADIVINASTE!")
        break

print(f'Has adivinado en {contador} intentos')

    



