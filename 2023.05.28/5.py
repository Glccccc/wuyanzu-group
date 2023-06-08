from pathlib import Path
from datetime import datetime as dt
    
def logger(function: 'callable') -> 'callable':

    """Фукнкция декоратор, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции"""
    
    file_path = Path(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data\function_calls.log')
    
    def wrapper(*args, **kwargs) -> 'any':
    
        now = dt.now()
        now.strftime('%Y.%m.%d %H:%M:%S')
        
        arguments =[f'{arg}' for arg in args] + [f'{k}={v}' for k, v in kwargs.items()] 
                
        if function.__defaults__ is not None:
            for def_arg in function.__defaults__:
                if function.__code__.co_argcount != len(args):
                    arguments += [f'{def_arg}']                    
               
        if function.__kwdefaults__ is not None:
            for k, v in function.__kwdefaults__.items():
                if k not in kwargs:
                    arguments += [f'{k}={v}']
                    
        print_log = f'{now.strftime("%Y.%m.%d %H:%M:%S")} - {function.__name__}({", ".join(arguments)}) -> '
        
        with open(file_path, mode = 'a', encoding = 'utf-8') as filein:
            filein.write(print_log)
        
        try: 
            print(result := function(*args, **kwargs))
            with open(file_path, mode = 'a', encoding = 'utf-8') as filein:
                filein.write(f'{result}\n')
        except Exception as exception:
            log_exception = f'{type(exception).__name__}: {str(exception)}'
            print(f'\t{type(exception).__name__}:', str(exception))
            with open(file_path, mode = 'a', encoding = 'utf-8') as filein:
                filein.write(f'{log_exception}\n')             
     
    return wrapper
    
# D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28>python -i 5.py
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=4)
# 0.6667
# >>> div_round(2, 0, digits=4)
        # ZeroDivisionError: division by zero
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()
# None
# >>>

# 2023.06.08 15:48:05 - div_round(2, 3, digits=4) -> 0.6667 
# 2023.06.08 15:48:09 - div_round(2, 0, digits=4) -> ZeroDivisionError: division by zero
# 2023.06.08 15:49:14 - testing_function() -> None 