num_position = int(input('Введите разряд числа: '))
max_num = int(num_position * '9')
count_numbers = 0

for num in range((max_num + 1) // 10, max_num + 1):
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else: 
        count_numbers += 1

print(count_numbers)        

# Введите разряд числа: 3
# 143

# Введите разряд числа: 4
# 1061

# Введите разряд числа: 5
# 8363
