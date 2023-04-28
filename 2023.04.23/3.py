num = int(input('Введите число: '))
# любое число делится на 1 и на самого себя, поэтому range последовательность будет от 2 до num НЕвключая
# если число n имеет делитель d, то оно также имеет делитель n/d. поэтому достаточно искать делители только до квадратного корня числа n
summa_divisors = 1 + num

for divisors in range(2, num):
    if divisors ** 2 == num:
        summa_divisors += divisors
        break
    elif divisors ** 2 <= num:
        if num % divisors == 0:
           summa_divisors += divisors + num // divisors
                   
print(summa_divisors)

# Введите число: 50
# 93

