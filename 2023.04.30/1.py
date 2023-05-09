email_inp = input(' Введите адрес электронной почты: ')
# адрес электронной почты не может начинатсья или заканчиватся с '.' , '@'. Cимвол '@' должен быть только один, и после него должен быть символ '.'
# если еще проверять что содержит только латинские буквы, цифры, определенные символы, тогда решаем через множества
latin_chars_digit = {chr(code) for code in range(97, 123)} |\
                    {'@','.','!','#','$','%','&','*','+','-','/','=','?','^','_','`','{','|','}','~'} |\
                    {str(digit) for digit in range(0, 10)}
                  
email_set = set((email_inp).lower())
if (email_set < latin_chars_digit): 
    if (
            email_inp[0] != '@'
        and email_inp[0] != '.'
        and email_inp[len(email_inp)-1] != '.'
        and email_inp.count('@') == 1
        and email_inp.count('.') > 0
        and email_inp.rindex('.') > email_inp.index('@')
        and email_inp.rindex('.') != email_inp.index('@') + 1
    ):  
        print('Да')
    else:
        print('Нет')
else:
    print('Нет')
    
# рафикова@mail.ru
# Нет

# fdfs@.sdfa
# Нет

# liliya_123@mail.com.ru
# Да

# @dsd.sf
# Нет

# .sff@fdf.df
# Нет

# aaa@sad@ad.fsf
# Нет

# sffdf@dfg.dgdg.dg
# Да

# svd.dsgsdg@dgdsd.dg.sf
# Да

# sfasf
# Нет

