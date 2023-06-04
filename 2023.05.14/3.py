def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list:

    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или изменённую копию"""
        
    if copy:
        numbers = numbers.copy()
    for _ in range(n):
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))       
    
    return numbers    
        
# >>> nums =[10,20,30,40,50,60,70]
# >>> nums_test= numbers_strip(nums, 3, copy=True)
# >>> nums_test
# [40]
# >>> nums is nums_test
# False
# >>> nums
# [10, 20, 30, 40, 50, 60, 70]
# >>>


# >>> nums =[10,20,30,40,50,60,70]
# >>> nums_test= numbers_strip(nums)
# >>> nums
# [20, 30, 40, 50, 60]
# >>> nums is nums_test
# True
# >>> nums
# [20, 30, 40, 50, 60]
# >>>