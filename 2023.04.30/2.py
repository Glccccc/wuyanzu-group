fruits = []

while True:
    fruit = input(' Введите фрукт: ')
    if not fruit:
        break
    fruits.append(fruit)

if len(fruits) >= 2:
    fruits = fruits[:-2] + [' и '.join(fruits[-2:])]

print(*fruits, sep = ', ')

# яблоко
# яблоко и груша
# груша, яблоко и арбуз
# яблоко, груша, слива и арбуз

