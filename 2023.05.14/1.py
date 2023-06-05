def strong_password(password: str) -> bool:

    """Проверяет и возвращает объект true если пароль надежный, иначе возвращает объект false."""
    
    password_set = set(password)
    lower_set = {chr(code) for code in range(97, 123)}
    upper_set = {chr(code) for code in range(65, 91)}
    # digit_set = {str(digit) for digit in range(0, 10)}
    digit_set = set('0123456789')
    # chars_set = {'!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','\{','\|','\}','~',' '}
    chars_set = set('!\"#$%&\'()*+,-./:;<=>?@[\\]^_`\{\|\}~ ')
    total_set = lower_set | upper_set | digit_set | chars_set
    
    if password_set <= total_set and len(password) >= 8:
        digit_count = 0
        
        for char in password:
            if char.isdigit():
                digit_count += 1
            
        return bool(
            password_set & upper_set and
            password_set & lower_set and
            password_set & digit_set and
            password_set & chars_set and
            digit_count >= 2
        )
    else:
        return False
 

# >>> strong_password('lili_56kad')
# False
# >>> strong_password('lili_56kaD')
# True
# >>> strong_password('lili_5kaD')
# False
# >>> strong_password('lili_kaD')
# False
# >>> strong_password('Lili_56')
# False
# >>> strong_password('Lili_56a')
# True
# >>> strong_password('РафиковаLiliya_89FM')
# False