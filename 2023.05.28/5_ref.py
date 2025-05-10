from datetime import datetime as dt  # 导入datetime用于获取当前时间

import utils_ref  # 导入自定义工具模块

log_path = utils_ref.DATA_DIR / 'function_calls.log'  # 日志文件路径


def logger(func_obj: 'function') -> 'function':
    # 检查并初始化默认参数
    if func_obj.__defaults__ is None:
        func_obj.__defaults__ = ()
    if func_obj.__kwdefaults__ is None:
        func_obj.__kwdefaults__ = {}
    
    def wrapper(*args, **kwargs):
        flag_exc = False  # 标记是否发生异常
        timestamp = dt.now()  # 获取当前时间
        try:
            result = func_obj(*args, **kwargs)  # 调用被装饰函数
        except Exception as exc:
            result = f'{exc.__class__.__name__}: {exc}'  # 捕获异常信息
            flag_exc = True
        
        # 处理参数，生成参数字符串
        i = len(args) - func_obj.__code__.co_argcount
        args = ', '.join(
            str(arg)
            for arg in args + (func_obj.__defaults__[i:] if i else ())
        )
        kwargs = ', '.join(
            f'{key}={val}'
            for key, val in (func_obj.__kwdefaults__ | kwargs).items()
        )
        
        ins1 = ', ' if args and kwargs else ''
        ins2 = '..' if flag_exc else '->'
        # 写入日志文件
        with open(log_path, 'a', encoding='utf-8') as fileout:
            print(
                (f'{timestamp:%Y.%m.%d %H:%M:%S}'
                 f' — {func_obj.__name__}({args}{ins1}{kwargs})'
                 f' {ins2} {result}'), 
                file=fileout
            )
        return result  # 返回函数结果
    
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


# >>> @logger
# ... def test1(a, b, c):
# ...     print(f'PRINT: {a=}, {b=}, {c=}')
# ... 
# >>> 
# >>> test1(1, 2, 7)
# PRINT: a=1, b=2, c=7
# >>>
# >>> print(log_path.read_text())
# 2023.10.28 23:05:08 — test1(1, 2, 7) -> None
# 
# >>>
