from pathlib import Path  # 导入Path类用于处理文件和目录路径


# ИСПРАВИТЬ: в возвращаемом кортеже может быть произвольное количество строк, а вы аннотировали ровно одну
# 修正：返回的元组可以有任意数量的字符串，类型注解应为tuple[str, ...]
def list_files(path_user: str) -> tuple[str] | None:
    """Возвращает кортеж с именами файлов в каталоге по переданному пути. В случае, если по переданному пути отсутствует каталог, функция возвращает None"""
    # 将用户传入的路径字符串转换为Path对象
    dir_path = Path(path_user)
    # 判断该路径是否为目录
    if dir_path.is_dir():
        # 生成一个元组，包含目录下所有文件的文件名（不包括子目录）
        files = tuple(file.name for file in dir_path.iterdir() if file.is_file())
        return files
    # 如果不是目录，函数默认返回None

# КОММЕНТАРИЙ: лишние переменные
# 注释：变量files其实可以省略，直接return即可


# >>> print(list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\datas'))
# None
# >>> list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28')
# ('# HW 2023.05.28.txt', '1.py')
# >>> list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>>


# ИТОГ: хорошо — 3/4
# 总结：实现良好 — 3/4
