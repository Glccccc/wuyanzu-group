def repeat(function: 'callable') -> 'callable':

    """Декоратор, который выполняет декорируемую функцию десять раз"""
    
    def wrapper(*args, **kwargs) -> 'any':
        for _ in range(10):
            function(*args, **kwargs)
            
    return wrapper
    
    
# @repeat   
# def testing_function():
    # print('python')
  
# testing_function()


# >>> def testing_function():
# ...     print('rafikova')
# ...
# >>> testing_function = repeat(testing_function)
# >>> testing_function()
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# rafikova
# >>>