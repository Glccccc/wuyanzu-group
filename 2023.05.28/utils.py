from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import shutil
from sys import path, modules


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
    shutil.copy2(file_path, Path(path[0]))

    # путь к импортируемому файлу
    # КОММЕНТАРИЙ: функция copy2() возвращает путь к копии файла в новом расположении
    importing_file_path = Path(path[0]) / file_path.name
    # название модуля - имя файла без расширения 
    module_name = file_path.stem
    # создание объекта спецификации
    spec = spec_from_file_location(module_name, importing_file_path)
    # создание объекта модуля
    module_obj = module_from_spec(spec)
    # добавление модуля в системный словарь
    modules[module_name] = module_obj
    # выполнение модуля
    spec.loader.exec_module(module_obj)
    
    return modules[module_name]

