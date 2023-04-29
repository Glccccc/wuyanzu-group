text = input('Введите текст: ')
price = 30
total_price = 0
for i in range(len(text)):
    if text[i] == ' ':
        continue
    else:
        total_price += price

print(f'{total_price // 100} руб. {total_price % 100} коп.')

# Введите текс: грузите       апельсины       бочках     братья         карамазовы
# 11 руб. 40 коп.