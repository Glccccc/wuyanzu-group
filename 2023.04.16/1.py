num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
num_3 = input('Введите третье число: ')
summa_positiv = 0

# КОММЕНТАРИЙ: очень хороший вариант решения — молодец
# isdecimal() позволит дополнительно отсеять отрицательные числа, поэтому проверку на > или < 0 не делаем.
if num_1.replace('.', '', 1).isdecimal():
    summa_positiv += float(num_1)

if num_2.replace('.', '', 1).isdecimal():
    summa_positiv += float(num_2)

if num_3.replace('.', '', 1).isdecimal():
    summa_positiv += float(num_3)      

print(f'{summa_positiv:.1f}')


# Введите первое число: -23
# Введите второе число: 2.3
# Введите третье число: 1
# 3.3


# ИТОГ: отлично — 4/4
