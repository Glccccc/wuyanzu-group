text = input('Введите текс: ')
price = 30

for i in range((len(text)) - 1):
    if text[i] == ' ':
        continue
    else:
        price += 30

print(f'{price // 100} руб. {price % 100} коп.')

# Введите текс: грузите       апельсины       бочках     братья         карамазовы
# 11 руб. 40 коп.