def countable_nouns(number: int, words: tuple[str, str, str]) -> str:

    """Возвращает строку, которая согласуется с переданным аргументом number"""
         
    list_1 = [2, 3, 4]
    list_2 = [0, 5, 6, 7, 8, 9]

    # ИСПРАВИТЬ: избыточно
    if 11 <= number % 100 <= 14:
        return words[2]
    elif number % 10 in list_1:
        return words[1]
    elif number % 10 in list_2:
        return words[2]
    else:
        return words[0]


# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(48, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(55, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(31, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(14, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(363, ("год", "года", "лет"))
# 'года'


# ИТОГ: хорошо — 2/2
