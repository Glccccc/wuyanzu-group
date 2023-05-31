def math_function_resolver(math_fun: 'callable', *numbers: tuple[float], strings: bool=False) -> list[float | str]:

    """Вычисляет округлённые значения для различных математических функций.
    :param math_fun: Вызываемый объект. Принимает один позиционно-ключевой аргумент — число x, для которого необходимо вычислить значение математической функции.
    :param numbers: Кортеж объектов int или float, передаваемых в вызываемый объект
    :param strings: Строго ключевой параметр, передаётся в виде объекта bool, значение по умолчанию False. Возвращает строковое представление результатов вычисления если передано значение True
    :return: Список результатов вычисления переданной функции."""

    result = []
    
    for num in numbers:
        result.append(round(math_fun(num), 2))
            
    return [str(num) for num in result] if strings else result
    
# >>> math_function_resolver(lambda x: 2**x, *range(1, 3), strings=True)
# ['2', '4']
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
# >>> math_function_resolver(lambda x: x**3, *(1,2,3,4,5),strings=True)
# ['1', '8', '27', '64', '125']
# >>>
