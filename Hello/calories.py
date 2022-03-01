# What you'll build
# In this challenge, you build a calorie counter that prompts the user for:

# The current date (in any format)
# Breakfast calories eaten
# Lunch calories eaten
# Dinner calories eaten
# Snack calories eaten
# The program will then sum up all of the calories and format them into a message.

print('Date (dd/mm/yyyy): ')
fecha = input()

print('Breakfast Calories: ')
cal_breakfast = int(input())

print('Lunch Calories: ')
cal_lunch = int(input())

print('Dinner Calories: ')
cal_dinner = int(input())

print('Snack Calories: ')
cal_snack = int(input())

total_cal = cal_breakfast + cal_lunch + cal_dinner + cal_snack

print('Las calorías consumidas del día '+ fecha + ' son: ' + str(total_cal) + ' kcal')
print('Para tener una dieta balanceada necesitas un promedio de 2000 kcal al día')