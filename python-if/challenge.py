
question = input('Would you like to continue?').lower()

if question == 'yes' or question == 'y':
    print('Continuing...')
elif question == 'no' or question == 'n':
    print('Exiting...')
else:
    print('Please try again and respond with yes or no.')
    
print('Complete!')