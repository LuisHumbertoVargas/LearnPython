num1 = input('Ingresa primer número a operar: ');
num2 = input('Ingresa segundo número a operar: ');

if (num1.isnumeric == False or num2.isnumeric == False) :
    print('Alguno de los datos ingresados es inválido, por favor revisa que sean números.');
    exit();
else:
    num1 = float(num1);
    num2 = float(num2);

    print('Qué operación deseas realizar?');
    print('Elije un número: ');
    operacion = int(input(' 1) Sumar \n 2) Restar \n 3) Multiplicar \n 4) Dividir \n 5) Exponenciar \n 6) Módulo \n'));
    
    
    if (operacion == 1) :
        resultado = num1 + num2;
        resutlado = round(resultado, 2);
        print('Suma = '+str(resultado));
    elif(operacion == 2) :
        resultado = num1 - num2;
        resutlado = round(resultado, 2);
        print('Resta = '+str(resultado));
    elif(operacion == 3) :
        resultado = num1 * num2;
        resutlado = round(resultado, 2);
        print('Multiplicación = '+str(resultado));
    elif(operacion == 4) :
        if (num2 == 0):
            print('No se puede dividir entre cero');
            exit();
        else:    
            resultado = num1 / num2;
            resutlado = round(resultado, 2);
            print('División = '+str(resultado));
    elif(operacion == 5) :
        resultado = num1 ** num2;
        resutlado = round(resultado, 2);
        print('Exponenciación = '+str(resultado));
    elif(operacion == 6) :
        resultado = num1 % num2;
        print('Exponenciación = '+str(resultado));
    else:
        print('Operación no reconocida');
        exit();
    



