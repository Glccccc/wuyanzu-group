text = input('Введите текст: ')

chars = '.,:;!?–—\'\"()*/'

text_new = ''.join([char for char in text if char not in chars])

print(text_new)

# Ра.фи,ко:ва; Ли!ли?я М/а*ра'то"в(н)а
# Рафикова Лилия Маратовна