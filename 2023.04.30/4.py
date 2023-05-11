dict_inp = {}

while True:
    dict_pair = input(' Введите ключ и значение через пробел: ').split()
    
    if not dict_pair:
        break
        
    dict_inp[dict_pair[0]] = dict_pair[1]

inp_value = input(' Введите значение из словаря: ')

if key := {k for k in dict_inp  if dict_inp[k] == inp_value}:
    print(*key)
else:
    print('! value error !')
    
# 123 арбуз
# 124 груша
# 125 слива
# 126 апельсин
# 126 ананас
# 127 манго
# Введите строку из словаря: слива
# 125 

# Введите строку из словаря: киви
# ! value error !


# 123 груша
# 124 груша
# 125 манго
# 126 слива
# 127 арбуз
# Введите значение из словаря: груша
# 123 124