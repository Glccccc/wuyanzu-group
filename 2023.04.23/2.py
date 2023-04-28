numbers_count = int(input('Введите количество чисел: '))
summa_positiv = 0

while numbers_count > 0:    
    num = int(input('Введите число: '))
    if num > 0:
        summa_positiv += num
    numbers_count -= 1
    
print(summa_positiv)

# Введите число: -10
# Введите число: 2
# Введите число: 30
# Введите число: -1
# Введите число: 0
# 32