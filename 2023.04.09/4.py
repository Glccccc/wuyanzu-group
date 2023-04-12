number = int(input('Введите трехзначное число: '))
num_1 = number % 10
num_2 = (number // 10) % 10
num_3 = (number // 100) % 10

print(f"Сумма цифр = {num_1 + num_2 + num_3}")
print(f"Произведение цифр = {num_1 * num_2 * num_3}")

# Сумма цифр = 12
# Произведение цифр = 64