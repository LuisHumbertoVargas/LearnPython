import random 

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  name = input('Enter a name, or \'q\' to quit:  ' )

  # Continue nos regresa al incio de la expresión booleana while
  if name.strip() == '':
    continue
  # break sale de la expresión booleana while antes de que se evalue como false 
  if name.strip() == 'q':
      break # Nota que tiene un espacio sino no funciona
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')