num_position = int(input('Введите разряд числа: '))
max_num = int(num_position * '9')
count_numbers = 0

for num in range((max_num + 1) // 10, max_num + 1):
    # ИСПОЛЬЗОВАТЬ: всегда лучше называть вещи своими именами: например, делитель — делителем =)
    # КОММЕНТАРИЙ: а имена переменных i, j, k традиционно используются почти только для индексов
    div = 2
    while div * div <= num:
        if not num % div:
            break
        div += 1
    else: 
        count_numbers += 1

print(count_numbers)        


# Введите разряд числа: 3
# 143

# Введите разряд числа: 4
# 1061

# Введите разряд числа: 5
# 8363


# ИТОГ: отлично — 5/5
