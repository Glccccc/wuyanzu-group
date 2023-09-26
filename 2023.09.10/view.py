"""
Представление MVC приложения.
""" 

class CLI:

    """Реализует представление MVC приложения"""
    
    @staticmethod
    def input_email() -> str:
    
        """Ввод в stdin email адреса"""        
        email = input("Введите email адрес: ")
        return email        

    @staticmethod
    def invalid_email() -> None:
    
        """Вывод в stdout сообщения о некорректном адресе"""
        print('Некорректный адрес')        
    
    @staticmethod
    def save_email() -> None:
    
        """Выводит в stdout сообщения об успешном сохранении адреса"""        
        print("Email успешно добавлен")
   
