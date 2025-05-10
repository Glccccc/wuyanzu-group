from pathlib import Path  # 导入Path类用于处理文件和目录路径


def list_files(dir_path: str) -> tuple[str, ...] | None:
    # 将传入的字符串路径转换为Path对象，方便后续操作
    dir_path = Path(dir_path)
    # 如果路径不是一个目录，则返回None
    if not dir_path.is_dir():
        return None
    
    # 返回目录下所有文件的文件名，组成一个元组
    return tuple(
        file.name  # 获取文件名
        for file in dir_path.iterdir()  # 遍历目录下的所有内容
        if file.is_file()  # 只保留文件，忽略子目录
    )


# 示例用法：
# data_path = r'd:\G-Doc\TOP Academy\Python web\! Задачи\7. Импорт модулей, работа с путями, файловый ввод-вывод\data'
# list_files(data_path)
# 返回：('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')

