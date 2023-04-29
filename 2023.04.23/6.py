ticket_number = input('Введите шестизначный номер билета: ')
sum_1, sum_2 = 0, 0

for i in range(6):
    if i < 3:
        sum_1 += int(ticket_number[i])
    else:
        sum_2 += int(ticket_number[i])   

print('ДА' if sum_1 == sum_2 else 'НЕТ')

# Введите номер билета: 401367
# НЕТ

# Введите номер билета: 183534
# ДА