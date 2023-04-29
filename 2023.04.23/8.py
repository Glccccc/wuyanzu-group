numbers_count = int(input('Введите количество чисел: '))
fibonacci = []
num, next_num = 1, 1

for i in range(numbers_count):
    fibonacci.append(num)
    num, next_num = next_num, num + next_num

print(*fibonacci)

# Введите количество чисел: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597