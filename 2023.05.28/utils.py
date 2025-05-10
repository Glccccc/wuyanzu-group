from importlib.util import spec_from_file_location, module_from_spec  # 导入用于动态导入模块的工具
from pathlib import Path  # 导入Path用于路径处理
import shutil  # 导入shutil用于文件操作
from sys import path, modules  # 导入sys.path和sys.modules


def important_message(message: str) -> str:
    """Возвращает сгенерированную строку, переданную в параметры функции"""
    width = shutil.get_terminal_size().columns - 3
    line1 = f'#{"="*width}#'
    line2 = f'\n#{" "*width}#\n'

    text_line = []
    temp_line = ''
    for word in message.split():
        if len(temp_line  + word) > width - 4:
            text_line += f'#{temp_line.center(width)}#\n'
            temp_line = ''
        temp_line += f'{word} '
    text_line += f'#{temp_line.center(width)}#'   
    
    message_out = line1 + line2 + ''.join(text_line) + line2 + line1 
    
    return message_out


def load_file(file_path: str | Path) -> '< module >':
    """Осуществляет копирование файла по переданному пути в текущей каталог, импортирует файл и возвращает объект модуля, созданного при импортировании файла."""

    # копирование файла по переданному пути в текущей каталог
    shutil.copy2(file_path, Path(path[0]))  # 复制文件到当前目录

    # путь к импортируемому файлу
    # КОММЕНТАРИЙ: функция copy2() возвращает путь к копии файла в новом расположении
    importing_file_path = Path(path[0]) / file_path.name  # 构造新文件路径
    # название модуля - имя файла без расширения 
    module_name = file_path.stem  # 获取模块名
    # создание объекта спецификации
    spec = spec_from_file_location(module_name, importing_file_path)  # 创建模块规范
    # создание объекта модуля
    module_obj = module_from_spec(spec)  # 创建模块对象
    # добавление модуля в системный словарь
    modules[module_name] = module_obj  # 注册到sys.modules
    # выполнение модуля
    spec.loader.exec_module(module_obj)  # 执行模块
    
    return modules[module_name]  # 返回模块对象

