"""
Контроллер MVC приложения.
""" 

import model
import view  
    
class Application():

    """Реализует контроллер MVC приложения"""

    def save_email(self, email: str) -> None:
    
        """Сохраняет переданный email адрес"""
        
        try: 
            self.email = model.Email(email)
            model.FileIO.add_email(email)
            view.CLI.save_email()
        except ValueError as ex:
            view.CLI.invalid_email()
            
    def input_email(self) -> None:
     
        """Реализует условно-бесконечный цикл получения адресов от пользователя, с выходом из цикла по вводу пустой строки"""
        
        while True:
            email = view.CLI.input_email()
            if email == "":
                break
            self.save_email(email)
            
            
