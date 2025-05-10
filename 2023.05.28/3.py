from pathlib import Path  # 导入Path类用于处理文件和目录路径
from utils import load_file  # 从utils模块导入load_file函数


def ask_for_file() -> '< module >':
    """
    向用户请求丢失文件的路径，验证文件存在后，调用load_file函数复制并导入该文件，返回模块对象。
    """
    while True:
        path_input = Path(input(' Введите путь к файлу: '))  # 提示用户输入文件路径
        if path_input.is_file():  # 判断路径是否为文件
            break
        else:
            print('! Ошибка, не существует файл по указанному пути !')  # 错误提示
        
    return load_file(path_input)  # 调用load_file复制并导入文件，返回模块对象


# D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28>python -i 3.py
# >>> config_module = ask_for_file()
#  Введите путь к файлу: d:\student\2023.05.28\conf.py
# ! Ошибка, не существует файл по указанному пути !
#  Введите путь к файлу: D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data
# ! Ошибка, не существует файл по указанному пути !
#  Введите путь к файлу: D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
# >>>

# >>> module = ask_for_file()
#  Введите путь к файлу: d:\G-Doc\YandexDisk\Scripts\_Singles\si_unit.py
# >>>
# >>> module.SIUnit
# <class 'si_unit.SIUnit'>

# КОММЕНТАРИЙ: очень одобряю более гибкую реализацию функции load_file()


# ИТОГ: отлично — 6/6
