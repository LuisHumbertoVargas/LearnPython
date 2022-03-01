# print(type('Hello world'))
# print(type(7))

# print(type(True))
# print(type(False))

# print(type('True'))
# print(type('False'))

# Regresa TRUE para los strings que tienen algo
# aunque sea espacios en blanco como el 4to print
# print(bool('True'))
# print(bool('False'))
# print(bool(''))
# print(bool(' '))
# print(bool('Hello world!'))


# Regresa TRUE para los integers que tienen valor != 0
# print(bool(7))
# print(bool(1))
# print(bool(0))
# print(bool(-1))

# if (1 + 1) == 3:
#     print('correct')
# else: 
#     print('incorrect')

# Imprime falso o verdadero de acuerdo a las condicioens booleanas que colocamos
# print(1 + 1 == 3)
# print(1 + 1 == 2)

# print(3 == 4) # false
# print(3 != 4) # true

# print(3 > 4) # false
# print(3 < 4) # true
# print(3 >= 4) # false
# print(3 <= 4) # true

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value) # Cambia de TRUE a FALSE
print(not false_value) # Cambia de FALSE a TRUE

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')