def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list:

    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или изменённую копию"""
    
    for _ in range(0, n):
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))       
    
    return numbers.copy() if copy else numbers   
    # заменила на тернарный оператор
    # if copy:
        # return numbers.copy()
    # else:
        # return numbers
       
     
# >>> nums =[10,20,30,40,50,60,70]
# >>> nums_test= numbers_strip(nums, 3, copy=True)
# >>> nums_test
# [40]
# >>> nums is nums_test
# False
# >>>
# >>> sample = [1,2,3,4,5,6,7]
# >>> nums_test= numbers_strip(sample)
# >>> nums_test
# [2, 3, 4, 5, 6]
# >>> sample is nums_test
# True
