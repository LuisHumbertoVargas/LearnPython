# print(type('7'))
# print(type(7))
# print(type(7.1))

# print(isinstance('7', str))
# print(isinstance(7, int))
# print(isinstance(7.1, float))

# print(isinstance(7, str))
# print(isinstance('7', int))
# print(isinstance('7.1', float))

fahrenheit = input("Ingresa una temperatura (°F): ");

if fahrenheit.isnumeric() == False :
    print('El valor ingresado no es válido (numérico): ');
    exit();
else :
    fahrenheit = float(fahrenheit);
    # fórmula matemática para convertir Fahrenheit a Celsius 
    celsius = (fahrenheit - 32) * (5/9);
    celsius = round(celsius, 2);
    print('Temperatura: ' + str(celsius) + ' °C');



