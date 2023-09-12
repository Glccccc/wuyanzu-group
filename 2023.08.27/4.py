from dataclasses import dataclass
from os import name as os_name
from typing import Self

if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:

    """Файл в файловой системе."""
    
    name: str
    dir_path: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        
        """Возвращает путь к файлу в виде строки."""
    
        return self.dir_path + PATH_SEP + self.name


class Folder(list):

    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    
    def __init__(self, name: str, dir_path: str):
        super().__init__()
        self.name = name
        self.dir_path = dir_path
            
    
    def add_elements(self, name: File | Self):
        
        """Добавляет файл или каталог в текущий каталог"""
        
        self.append(name)
        name.dir_path = self.dir_path + PATH_SEP + self.name        
            

    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name   
    
       

def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())
        
# не разобралась до конца   
     
# >>> d1 = Folder('Python','d:')
# >>> d2 = Folder('DZ', '')
# >>> d1.add_elements(d2)
# >>> f1 =File('1.py','')
# >>> d2.add_elements(f1)
# >>> f2 =File('2.py','')
# >>> d1.add_elements(f2)
# >>> ls(f2)
# d:\Python\2.py
# >>> ls(f1)
# d:\Python\DZ\1.py
# >>> ls(d2)
# d:\Python\DZ
# >>>