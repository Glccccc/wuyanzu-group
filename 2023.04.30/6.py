set_binary_nums = {'0', '1', 'b'}
inp_num = input(' Введите число: ')
set_inp_num = set(inp_num)

if inp_num == 'b' or inp_num == '0b' or inp_num == '1b':
    print('Нет')
elif set_inp_num <= set_binary_nums and 'b' not in set_inp_num:
    print('Да')
elif (
       set_inp_num <= set_binary_nums
    and inp_num[0] != '1'
    and inp_num.count('b') == 1
    and (inp_num.index('b') == 1 or inp_num.index('b') == 0)
):   
    print('Да')
else:
    print('Нет')

# Убрала условие len(inp_num) >= 2: почему то всегда думала что 0 в двоичной это 00, а 1 - 01. век живи-век учись))


# Введите число: 0101
# Да
# Введите число: b11
# Да
# Введите число: 0b11001
# Да
# Введите число: 1b0101
# Нет
# Введите число: 01
# Да
# Введите число: 11
# Да
# Введите число: 1
# Да
# Введите число: 0
# Да
# Введите число: 0b003b
# Нет

