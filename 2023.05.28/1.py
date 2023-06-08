from pathlib import Path
    
def  list_files(path_user: str) -> tuple[str] | None:
    
    """Возвращает кортеж с именами файлов в каталоге по переданному пути. В случае, если по переданному пути отсутствует каталог, функция возвращает None"""
    
    dir_path = Path(path_user)
    
    if dir_path.is_dir():
    
        files = tuple(file.name for file in dir_path.iterdir() if file.is_file())
        
        return files
    
# >>> print(list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\datas'))
# None
# >>> list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28')
# ('# HW 2023.05.28.txt', '1.py')
# >>> list_files(r'D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>>
