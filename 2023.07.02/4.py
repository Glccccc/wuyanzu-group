import csv
from pathlib import Path
from sys import path

class CountableNouns:
   
    """Предоставляет интерфейс для работы с файловой базой существительных"""
   
    db_path: Path = Path(path[0]) / 'words.csv'
    words: dict[str, tuple[str, str]] = {}
            
    with open(db_path, "r", encoding='utf-8') as r_file:
        for row in csv.reader(r_file):
            row = tuple(row)
            words |= {row[0]: row[1:]}

  
    @classmethod
    def pick(self, number: int, word: str) -> str:
       
        """Принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное"""
        
        if word in self.words:          
            list_1= [2, 3, 4]
            list_2 = [0, 5, 6, 7, 8, 9]

            if 11 <= number % 100 <=14 or number % 10 in list_2:
                return self.words[word][1]
            elif number % 10 in list_1:
                return self.words[word][0]
            else:
                return word
        else:
            self.save_words(word)
       
    @classmethod
    def save_words(self, word1: str = None) -> None:
    
        """Запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных"""
       
        if word1 is not None:
            print(f'существительное \"{word1}" отсутствует в базе')        
        if word1 is None:
            word1 = input('введите слово, согласующееся с числительным "один": ')  
            
        word2: str = input(' введите слово, согласующееся с числительным "два": ')
        word3: str = input(' введите слово, согласующееся с числительным "пять": ')
        
        self.words[word1] = tuple([word2, word3])  

        with open(self.db_path, 'w', encoding='utf-8') as w_file:
            row = csv.writer(w_file, delimiter = ",", lineterminator='\n')
            row.writerows([k, *v] for k, v in self.words.items())
          

# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(1,'год')
# 'год'
# >>> CountableNouns.pick(8,'год')
# 'лет'
# >>> CountableNouns.pick(22,'год')
# 'года'
# >>> CountableNouns.pick(365,'день')
# 'дней'
# >>> CountableNouns.pick(2,'день')
# 'дня'
# >>> CountableNouns.pick(1,'день')
# 'день'
# >>> CountableNouns.pick(3,'месяц')
# 'месяца'
# >>> CountableNouns.pick(14,'месяц')
# 'месяцев'
# >>> CountableNouns.pick(11,'месяц')
# 'месяцев'
# >>> CountableNouns.pick(1,'месяц')
# 'месяц'
# >>> CountableNouns.pick(10,'машина')
# существительное "машина" отсутствует в базе
 # введите слово, согласующееся с числительным "два": машины
 # введите слово, согласующееся с числительным "пять": машин
# >>> CountableNouns.pick(10,'машина')
# 'машин'
# >>> CountableNouns.pick(22,'машина')
# 'машины'
# >>> CountableNouns.pick(33,'капля')
# существительное "капля" отсутствует в базе
 # введите слово, согласующееся с числительным "два": капли
 # введите слово, согласующееся с числительным "пять": капель
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'машина': ('машины', 'машин'), 'капля': ('капли', 'капель')}
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": попугай
 # введите слово, согласующееся с числительным "два": попугая
 # введите слово, согласующееся с числительным "пять": попугаев
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'машина': ('машины', 'машин'), 'капля': ('капли', 'капель'), 'попугай': ('попугая', 'попугаев')}
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# машина,машины,машин
# капля,капли,капель
# попугай,попугая,попугаев

# >>>