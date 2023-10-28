def central_tendency(num1: float, num2: float, /, *numbers: float) -> dict[str, float]:
    
    """Вычисляет и возвращает словарь с подписанными вычисленными значениями мер центральной тенденции"""

    numbers = sorted((num1, num2) + numbers)
    length_numbers = len(numbers)
    middle_index = length_numbers // 2
    # УДАЛИТЬ: у вас уже есть явный цикл по всем числам, не нужно выполнять ещё один
    arithmetic = sum(numbers) / length_numbers
    product = 1
    numerator = 0
    
    if length_numbers % 2:
        median = float(numbers[middle_index])
    else:
        median = sum(numbers[middle_index-1:middle_index+1]) / 2

    for n in numbers:
        product *= n
        # ИСПРАВИТЬ: необходимо предусмотреть возможность появления числа 0 среди входных чисел (см. тест ниже)
        numerator += 1 / n

    geometric = product ** (1 / length_numbers)
    harmonic = length_numbers / numerator

    dict_tendency = {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }
    return dict_tendency


# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>> 
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
# >>>
# >>> central_tendency(1, 2, 3, 4,5,6)
# {'median': 3.5, 'arithmetic': 3.5, 'geometric': 2.993795165523909, 'harmonic': 2.4489795918367347}
# >>>

# >>> central_tendency(-1, 0, -2, 1)
# ...
# ZeroDivisionError: division by zero


# ИТОГ: хорошо, доработать — 4/6
