num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
num_3 = input('Введите третье число: ')
summa_positiv = 0

if num_1.isdecimal():
    summa_positiv += int(num_1)
elif num_1.replace('.','',1).isdecimal():
    summa_positiv += float(num_1)

if num_2.isdecimal():
    summa_positiv += int(num_2)
elif num_2.replace('.','',1).isdecimal():
    summa_positiv += float(num_2)

if num_3.isdecimal():
    summa_positiv += int(num_3)
elif num_3.replace('.','',1).isdecimal():
    summa_positiv += float(num_3)
    
print(f'{summa_positiv:.1f}')

# Введите первое число: -23
# Введите второе число: 2.3
# Введите третье число: 1
# 3.3