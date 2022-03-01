def process_numbers(lista):    
    numeros = []    

    if isinstance(lista, list) == False:
        return numeros

    for value in lista:
        
        if isinstance(value, str) == False or value.isnumeric() != False:
            numeros.append(int(value))

    numeros.sort()
    return numeros

def process_names(lista):
    nombres = []

    if isinstance(lista, list) == False:
        return nombres

    for name in lista:
        
        if isinstance(name, str) != False and name.isnumeric() == False:
            nombres.append(name)

    nombres.sort()
    return nombres
