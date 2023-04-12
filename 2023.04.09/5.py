whole_part = input('Введите целую часть: ')
fractional_part = input('Введите дробную часть: ')

miles = float(f'{whole_part}.{fractional_part}')

print(f'{miles} миль = {miles * 1.61:.1f} км')

# 15.7 миль = 25.3 км