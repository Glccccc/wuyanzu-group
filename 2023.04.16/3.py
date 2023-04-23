year = input('Введите год: ')

if year.isdecimal():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('да')
    else:
        print('нет')
else:
    print('Ошибка, некорректный ввод')


# Введите год: 2020
# да

# Введите год: 2023
# нет


# ИТОГ: отлично — 3/3
