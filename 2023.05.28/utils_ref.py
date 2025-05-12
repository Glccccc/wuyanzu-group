from pathlib import Path  # 导入Path用于路径处理
from shutil import get_terminal_size as gts, copy2  # 导入终端尺寸获取和文件复制
from sys import path  # 导入sys.path
from types import ModuleType  # 导入ModuleType用于类型注解

import data.vars as data  # 导入数据模块

ROOT_DIR = Path(path[0])  # 项目根目录
DATA_DIR = ROOT_DIR / 'data'  # data目录路径


# для задачи 1
def important_message(text) -> str:
    # 获取终端宽度和边距
    width, padding = gts()[0] - 1, 2
    just = width - padding*2 - 2

    edge = '=' * (width-2)
    empty = ' ' * (width-2)
    
    words, lines, i = text.split(), [], 0
    while i < len(words):
        line = ''
        while i < len(words):
            if len(line + words[i]) > just:
                break
            line += words[i] + ' '
            i += 1
        lines += [line[:-1]]

    text = '\n'.join(
        f'#  {line.center(just)}  #'
        for line in lines
    )
    return (
        f'#{edge}#\n'
        f'#{empty}#\n'
        f'{text}\n'
        f'#{empty}#\n'
        f'#{edge}#'
    )


# для задачи 3
# 动态导入conf.py模块
# file_path: 需要导入的文件路径
# 返回：导入的模块对象

def load_file(file_path) -> ModuleType:
    copy2(file_path, ROOT_DIR)  # 复制文件到根目录
    import conf  # 动态导入conf模块
    return conf  # 返回模块对象

