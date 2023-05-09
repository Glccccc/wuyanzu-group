list_num1 = input(' Введите целые положительные числа через пробел: ').split()
list_num2 = input(' Введите целые положительные числа через пробел: ').split()

if list_num2 == '':
    print('Да')
elif len(list_num1) >= len(list_num2):
    try:
        if list_num2 == list_num1[list_num1.index((list_num2[0])) : list_num1.index((list_num2[0])) + len(list_num2)]:
            print('Да')
        else:
            print('Нет')
    # если индекс с элементом не найден
    except ValueError:
        print('Нет')
else:
    print('Нет')
    
# 1 2 3 4
# 1 2
# Да
   
# 1 2 3 4
# 2 4
# Нет
