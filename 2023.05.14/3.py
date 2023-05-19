def numbers_strip(numbers: list[float], n=1, *, copy=False):

    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или изменённую копию"""
    
    while n>0:
        max_num = max(numbers)
        min_num = min(numbers)
        
        for i in numbers:
            if max_num == i:
                numbers.remove(max(numbers))
            elif min_num == i:
                numbers.remove(min(numbers))
        n -= 1 
        
    if copy:
        return numbers.copy()
    else:
        return numbers
       
     
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
