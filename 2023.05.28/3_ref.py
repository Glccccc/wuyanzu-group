from pathlib import Path  # 导入Path类用于处理文件和目录路径
from types import ModuleType  # 导入ModuleType用于类型注解

import utils_ref  # 导入自定义工具模块

lost_file_name = 'conf.py'  # 需要查找的丢失文件名


def get_path_from_user() -> Path:
    while True:
        file_path = Path(input('путь: '))  # 提示用户输入文件路径
        # 判断路径是否为文件且文件名正确
        if file_path.is_file() and file_path.name == lost_file_name:
            return file_path
        print('! по указанному пути отсутствует необходимый файл !')  # 错误提示


def ask_for_file() -> ModuleType:
    # 调用get_path_from_user获取文件路径，并用utils_ref.load_file导入模块
    return utils_ref.load_file(get_path_from_user())


# >>> config_module = ask_for_file()
# путь: d:\G-Doc\TOP Academy\Python web\! Задачи\7. Импорт модулей, работа с путями, файловый ввод-вывод\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}

