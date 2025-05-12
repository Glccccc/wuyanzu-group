from datetime import datetime as dt  # 导入datetime用于获取当前时间


def logger(function: 'callable') -> 'callable':
    """
    装饰器函数：用于记录被装饰函数的调用日志，包括调用时间、参数、返回值或异常信息。
    """
    
    def wrapper(*args, **kwargs) -> 'any':
        # 记录当前时间
        now = dt.now()
        today = now.strftime('%Y.%m.%d %H:%M:%S')
        
        # 处理参数，生成参数字符串
        arguments = [f'{arg}' for arg in args] + [f'{k}={v}' for k, v in kwargs.items()]
        
        # 处理默认参数
        if function.__defaults__ is not None:
            for def_arg in function.__defaults__:
                if function.__code__.co_argcount != len(args):
                    arguments += [f'{def_arg}']
        
        # 处理关键字默认参数
        if function.__kwdefaults__ is not None:
            for k, v in function.__kwdefaults__.items():
                if k not in kwargs:
                    arguments += [f'{k}={v}']
        
        # 生成日志字符串
        print_log = f'{today} - {function.__name__}({", ".join(arguments)}) -> '

        # 打开日志文件，追加写入
        with open('data\\function_calls.log', mode='a', encoding='utf-8') as filein:
            filein.write(print_log)
            try:
                result = function(*args, **kwargs)  # 调用被装饰函数
                filein.write(f'{result}\n')  # 写入返回值
                return result
            except Exception as exception:
                log_exception = f'{type(exception).__name__}: {str(exception)}'
                print(f'\t{log_exception}')  # 控制台输出异常
                filein.write(f'{log_exception}\n')  # 写入异常信息
    
    return wrapper  # 返回包装后的函数


# 使用方法：
# 1. 定义一个函数，例如：
# def add(a, b):
#     return a + b
# 2. 使用logger装饰器：
# add = logger(add)
# 3. 调用add(1, 2)，会自动记录日志到data/function_calls.log
# 或者使用@logger语法糖：
# @logger
# def add(a, b):
#     return a + b
#
# 适用场景：
# 需要记录函数调用历史、调试、追踪异常等。


# D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28>python -i 5.py
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=4)
# 0.6667
# >>> div_round(2, 0, digits=4)
        # ZeroDivisionError: division by zero
# >>>

# 2023.06.09 09:17:51 - testing_function() -> None
# 2023.06.09 09:18:26 - div_round(2, 3, digits=4) -> 0.6667
# 2023.06.09 09:18:33 - div_round(2, 0, digits=4) -> ZeroDivisionError: division by zero


# ИТОГ: хорошо, но можно лучше — 4/6
