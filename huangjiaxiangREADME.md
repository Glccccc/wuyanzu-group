### 2023.04.09/文件下的任务、功能及使用方法：
1. **编写 name 函数**  
    
        *功能： 获取用户输入的姓名、姓氏和出生年份，并计算当前年龄，最后按照指定格式输出用户信息和年龄。  
        
        *参数：   
        -name：用户输入的名字，类型为 str。
        -lastname：用户输入的姓氏，类型为 str。
        -year：用户输入的出生年份，类型为 int。
       
        *返回值：*
        - 无返回值，直接通过 print 函数输出结果。
    
        *测试方法如下：
        name = input('Введите имя: ')
        lastname = input('Введите фамилию: ')
        year = int(input('Введите год рождения: '))

        print(lastname, name + ',', 2023 - year)
        
        *测试结果：
        -运行代码后，依次输入名字、姓氏和出生年份，程序会输出对应的格式化信息.
        假设输入如下：
        Введите имя: Лилия
        Введите фамилию: Рафикова
        Введите год рождения: 1989


        *输出结果为：
        Рафикова Лилия, 34


        #关于 input() 函数的返回值类型:
        input() 函数默认返回用户输入的内容作为字符串（str）类型。如果需要其他类型的数据，如整数或浮点数，需要显式地进行类型转换。
        例如：
        int(input())：将用户输入的字符串转换为整数。
        float(input())：将用户输入的字符串转换为浮点数。
        在代码中：
        name = input('Введите имя: ')：获取用户输入的名字，返回类型为 str。
        lastname = input('Введите фамилию: ')：获取用户输入的姓氏，返回类型为 str。
        year = int(input('Введите год рождения: '))：获取用户输入的出生年份，并将其转换为 int 类型。
2. **编写 number 函数**  

        *功能：接收用户输入的一个整数，然后输出该整数的下一个数和上一个数。

        *参数：
        -number：用户输入的整数，通过 input() 函数获取，并使用 int() 函数将其转换为整数类型。这是代码中唯一的变量参数。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，输入一个整数（例如 100）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 100，输出结果为：
        
        Cледующее за числом 100 число: 101
        Для числа 100 предыдущее число: 99
        输入 -5，输出结果为：
        
        Cледующее за числом -5 число: -4
        Для числа -5 предыдущее число: -6
        输入 0，输出结果为：
        
        Cледующее за числом 0 число: 1
        Для числа 0 предыдущее число: -1

        #代码解释：
        1.number = int(input('Введите число: '))：提示用户输入一个数字，并通过 input() 函数获取用户输入的字符串，然后使用 int() 函数将其转换为整数类型，存储到变量 number 中。
        2.print(f'Cледующее за числом {number} число: {number + 1}\n'：使用格式化字符串（f-string），将变量 number 和 number + 1 的值嵌入到字符串中，并输出。\n 是换行符，用于换行输出下一行内容。
        3.f'Для числа {number} предыдущее число: {number - 1}')：同样使用格式化字符串，将变量 number 和 number - 1 的值嵌入到字符串中，并输出。
3. **编写 minutes 函数** 

        *功能：将用户输入的分钟数转换为小时和分钟的形式，并输出结果。

        *参数：minutes：用户输入的分钟数，通过 input() 函数获取，并使用 int() 函数将其转换为整数类型。这是代码中唯一的变量参数。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，输入一个整数（例如 130）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 130，输出结果为：
        130 мин - это 2 час 10 мин
        输入 90，输出结果为：
        90 мин - это 1 час 30 мин
        输入 60，输出结果为：
        60 мин - это 1 час 0 мин
        输入 59，输出结果为：
        59 мин - это 0 час 59 мин

        #代码解释：
        1.minutes = int(input('Введите количество минут: '))
        提示用户输入一个数字，并通过 input() 函数获取用户输入的字符串。
        使用 int() 函数将输入的字符串转换为整数类型，存储到变量 minutes 中。

        2.print(f"{minutes} мин - это {minutes // 60} час {minutes % 60} мин")
        使用格式化字符串（f-string）输出结果。
        minutes // 60：计算小时数，使用整除运算符 //，结果为整数部分，表示完整的小时数。

        3.minutes % 60：计算剩余的分钟数，使用取模运算符 %，结果为除以 60 后的余数，表示不足一小时的分钟数。
        将 minutes、minutes // 60 和 minutes % 60 的值嵌入到字符串中，并输出。

4. **编写 number 函数** 

        *功能：接收用户输入的一个三位数，然后计算并输出该三位数各个位上的数字之和以及各个位上的数字之积。

        *参数：
        -number：用户输入的三位数，通过 input() 函数获取，并使用 int() 函数将其转换为整数类型。这是代码中唯一的变量参数。

        *返回值：
        代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，输入一个三位数（例如 123）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 123，输出结果为：
    
        Сумма цифр = 6
        Произведение цифр = 6
        输入 456，输出结果为：
    
        Сумма цифр = 15
        Произведение цифр = 120
        输入 100，输出结果为：

        Сумма цифр = 1
        Произведение цифр = 0

        #代码解释：
        1.number = int(input('Введите трехзначное число: '))
        提示用户输入一个数字，并通过 input() 函数获取用户输入的字符串。使用 int() 函数将输入的字符串转换为整数类型，存储到变量 number 中。

        2.num_1 = number % 10：计算个位数。使用取模运算符 %，结果为 number 除以 10 的余数，即个位数。num_2 = (number // 10) % 10：计算十位数。先用 number // 10 去掉个位数，再对 10 取模，得到十位数。num_3 = (number // 100) % 10：计算百位数。先用 number // 100 去掉个位和十位数，再对 10 取模，得到百位数。

        3.print(f"Сумма цифр = {num_1 + num_2 + num_3}")：计算各个位上的数字之和，并通过格式化字符串输出。print(f"Произведение цифр = {num_1 * num_2 * num_3}")：计算各个位上的数字之积，并通过格式化字符串输出。

5. **编写 whole_part和fractional_part  函数** 


        *功能：接收用户输入的整数部分和小数部分，将它们组合成一个浮点数（表示英里数），然后将其转换为公里数并输出结果。

        *参数：
        -whole_part：用户输入的整数部分，通过 input() 函数获取，存储为字符串类型。
        -fractional_part：用户输入的小数部分，通过 input() 函数获取，存储为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。
        
        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入整数部分和小数部分（例如整数部分输入 15，小数部分输入 7）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入整数部分 15，小数部分 7，输出结果为：
        15.7 миль = 25.3 км
        输入整数部分 10，小数部分 5，输出结果为：
        10.5 миль = 16.9 км
        输入整数部分 0，小数部分 5，输出结果为：
        0.5 миль = 0.8 км

        #代码解释：
        1.输入整数部分和小数部分：
        whole_part = input('Введите целую часть: ')：提示用户输入整数部分，并将其存储为字符串。
        fractional_part = input('Введите дробную часть: ')：提示用户输入小数部分，并将其存储为字符串。

        2.组合并转换为浮点数：
        miles = float(f'{whole_part}.{fractional_part}')：使用格式化字符串将整数部分和小数部分组合成一个完整的浮点数字符串（例如 15.7），然后通过 float() 函数将其转换为浮点数类型。

        3.计算并输出结果：
        print(f'{miles} миль = {miles * 1.61:.1f} км')：
        计算公里数：miles * 1.61，其中 1.61 是英里到公里的换算系数。
        使用格式化字符串输出结果，其中 :.1f 表示保留一位小数。

### 2023.04.16/文件下的任务、功能及使用方法：

1. **编写 num_1、num_2、num_3和 summa_positiv 函数** 

        *功能：接收用户输入的三个数，判断这些数是否为正数（包括正整数和正小数），并将所有正数相加，最终输出正数的总和。

        *参数：
        -num_1：用户输入的第一个数，通过 input() 函数获取，存储为字符串类型。

        -num_2：用户输入的第二个数，通过 input() 函数获取，存储为字符串类型。

        -num_3：用户输入的第三个数，通过 input() 函数获取，存储为字符串类型。

        -summa_positiv：用于存储正数的总和，初始值为 0

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入三个数（可以是正数、负数或小数）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 -23，2.3，1，输出结果为：3.3

        输入 -1，-2，-3，输出结果为：0.0

        输入 0，5，10.5，输出结果为：15.5

        输入 12.3，45.6，78.9，输出结果为：136.8

        #代码解释：
        1.输入三个数：
        num_1 = input('Введите первое число: ')：提示用户输入第一个数，并将其存储为字符串。
        num_2 = input('Введите второе число: ')：提示用户输入第二个数，并将其存储为字符串。
        num_3 = input('Введите третье число: ')：提示用户输入第三个数，并将其存储为字符串。

        2.判断是否为正数并累加：
        if num_1.replace('.', '', 1).isdecimal()：
        num_1.replace('.', '', 1)：将字符串中的第一个小数点移除（如果存在）。这是为了处理小数输入。
        .isdecimal()：检查移除小数点后的字符串是否只包含数字。如果是，则说明原字符串是一个正数（包括正整数和正小数）。
        如果是正数，则通过 float(num_1) 将字符串转换为浮点数，并将其加到 summa_positiv 中。
        同样的逻辑应用于 num_2 和 num_3。

        3.输出结果：
        print(f'{summa_positiv:.1f}')：将正数的总和输出到控制台，保留一位小数。

2. **编写 num_1与num_2  函数** 

        *功能：接收用户输入的两个整数，判断第一个数是否能被第二个数整除，并输出相应的结果。如果第二个数为零，则提示用户不能除以零。此外，代码还会检查用户输入是否为有效的整数。

        *参数：
        -num_1：用户输入的第一个数，通过 input() 函数获取，存储为字符串类型。
        -num_2：用户输入的第二个数，通过 input() 函数获取，存储为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入两个数（可以是整数或非整数）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 25 和 3，输出结果为：
        25 не делится на 3 нацело
        неполное частное: 8
        остаток: 1

        输入 8 和 2，输出结果为：
        8 делится на 2 нацело
        частное: 4

        输入 2 和 0，输出结果为：
        Ошибка, на ноль делить нельзя

        输入 abc 和 2，输出结果为：
        Ошибка, некорректный ввод

        #代码解释：
        1.输入两个数：
        num_1 = input('Введите первое число: ')：提示用户输入第一个数，并将其存储为字符串。
        num_2 = input('Введите второе число: ')：提示用户输入第二个数，并将其存储为字符串。

        2.检查输入是否为整数：
        if num_1.isdecimal() and num_2.isdecimal():：
        使用 isdecimal() 方法检查输入是否为非负整数。如果两个输入都是非负整数，则进入下一步。
        如果输入不合法（例如包含字母或负数），则输出错误信息：
        -Python-
        print('Ошибка, некорректный ввод')

        3.转换为整数并进行除法运算：
        num_1 = int(num_1) 和 num_2 = int(num_2)：将输入的字符串转换为整数。
        检查除数是否为零：
        -Python-
        if num_2 == 0:
            print('Ошибка, на ноль делить нельзя')
        如果除数为零，则直接输出错误信息并结束程序。
        如果除数不为零，则继续执行下一步。

        4.判断是否整除并输出结果：
        使用“海象运算符”（:=）计算余数：
        -Python-
        if remainder_modulo := num_1 % num_2:
            add1, add2, add3 = 'не ', 'неполное ', f'остаток: {remainder_modulo}'
        如果余数不为零，则说明不能整除，设置相应的提示信息。
        如果余数为零，则说明可以整除，不设置额外的提示信息。
        输出结果：
        -Python-
        print(f'{num_1} {add1}делится на {num_2} нацело\n'
            f'{add2}частное: {num_1 // num_2}\n'
            f'{add3}')

3. **编写  year  函数** 
        
        *功能：判断用户输入的年份是否为闰年。如果输入的年份是闰年，则输出“да”；如果不是闰年，则输出“нет”。此外，代码还会检查用户输入是否为有效的整数。

        *参数：
        -year：用户输入的年份，通过 input() 函数获取，初始为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，输入一个年份（可以是整数或非整数）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 2020，输出结果为：
        да
        输入 2023，输出结果为：
        нет
        输入 1900，输出结果为：
        нет
        输入 2000，输出结果为：
        да
        输入 abc，输出结果为：
        Ошибка, некорректный ввод

        #代码解释：
        1.输入年份：
        year = input('Введите год: ')：提示用户输入一个年份，并将其存储为字符串。

        2.检查输入是否为整数：
        if year.isdecimal():：
        使用 isdecimal() 方法检查输入是否为非负整数。如果输入是有效的整数，则继续下一步。
        如果输入不合法（例如包含字母或负数），则输出错误信息：
        -Python-
           print('Ошибка, некорректный ввод')

        3.转换为整数并判断是否为闰年：
        year = int(year)：将输入的字符串转换为整数。
        使用闰年的判断规则：
        -Python-
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('да')
        else:
            print('нет')
        闰年的条件是：
        年份能被4整除但不能被100整除。
        或者年份能被400整除。
        如果满足上述条件之一，则输出“да”；否则输出“нет”。

4. **编写 cell_1与cell_2  函数** 

        *功能：判断用户输入的两个国际象棋棋盘上的格子是否颜色相同。国际象棋棋盘由8×8的格子组成，每个格子用一个字母（a到h）和一个数字（1到8）表示。代码会检查输入的格子坐标是否有效，并判断这两个格子是否在同一颜色上。

        *参数：
        -cell_1：用户输入的第一个格子的坐标，通过 input() 函数获取，存储为字符串类型。
        -cell_2：用户输入的第二个格子的坐标，通过 input() 函数获取，存储为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入两个格子的坐标（例如 a1 和 b2）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 a1 和 b2，输出结果为：
        да
        输入 a1 和 a2，输出结果为：
        нет
        输入 h8 和 a1，输出结果为：
        нет
        输入 e5 和 e4，输出结果为：
        да
        输入 z9 和 a1，输出结果为：
        Ошибка, некорректный ввод

        #代码解释：
        1.输入两个格子的坐标：
        cell_1 = input('Введите координаты первой клетки: ')：提示用户输入第一个格子的坐标，并将其存储为字符串。
        cell_2 = input('Введите координаты второй клетки: ')：提示用户输入第二个格子的坐标，并将其存储为字符串。

        2.检查输入的坐标是否有效：
        使用多条件判断：
        -Python-
        if (
                'a' <= cell_1[0] <= 'h'
            and '1' <= cell_1[1] <= '8'
            and 'a' <= cell_2[0] <= 'h'
            and '1' <= cell_2[1] <= '8'
        ):
        检查第一个格子的字母部分是否在 a 到 h 之间。
        检查第一个格子的数字部分是否在 1 到 8 之间。
        检查第二个格子的字母部分是否在 a 到 h 之间。
        检查第二个格子的数字部分是否在 1 到 8 之间。
        如果任何一个条件不满足，则输出错误信息：
        -Python-
        print('Ошибка, некорректный ввод')

        3.判断两个格子是否颜色相同：
        使用 ord() 函数将字母转换为 ASCII 码值，然后加上数字部分的整数值：
        -Python-
        if (ord(cell_1[0]) + int(cell_1[1])) % 2 == (ord(cell_2[0]) + int(cell_2[1])) % 2:
        计算第一个格子的字母和数字之和的奇偶性。
        计算第二个格子的字母和数字之和的奇偶性。
        如果两个格子的奇偶性相同，则说明它们颜色相同，输出“да”；否则输出“нет”。

5. **编写 cell_1与cell_2 函数** 

        *功能：判断用户输入的两个国际象棋棋盘上的格子是否在同一行或同一列。国际象棋棋盘由8×8的格子组成，每个格子用一个字母（a到h）和一个数字（1到8）表示。代码会检查输入的格子坐标是否有效，并判断这两个格子是否在同一行或同一列。

        *参数：
        -cell_1：用户输入的第一个格子的坐标，通过 input() 函数获取，存储为字符串类型。
        -cell_2：用户输入的第二个格子的坐标，通过 input() 函数获取，存储为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入两个格子的坐标（例如 d4 和 e4）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 d4 和 e4，输出结果为：
        да
        输入 a2 和 c4，输出结果为：
        нет
        输入 a1 和 a8，输出结果为：
        да
        输入 h8 和 a1，输出结果为：
        нет
        输入 z9 和 a1，输出结果为：
        Ошибка, некорректный ввод

        #代码解释：
        1.输入两个格子的坐标：
        cell_1 = input('Введите координаты первой клетки: ')：提示用户输入第一个格子的坐标，并将其存储为字符串。
        cell_2 = input('Введите координаты второй клетки: ')：提示用户输入第二个格子的坐标，并将其存储为字符串。

        2.检查输入的坐标是否有效：
        使用多条件判断：
        -Python-
        if (
                'a' <= cell_1[0] <= 'h'
            and '1' <= cell_1[1] <= '8'
            and 'a' <= cell_2[0] <= 'h'
            and '1' <= cell_2[1] <= '8'
        ):
        检查第一个格子的字母部分是否在 a 到 h 之间。
        检查第一个格子的数字部分是否在 1 到 8 之间。
        检查第二个格子的字母部分是否在 a 到 h 之间。
        检查第二个格子的数字部分是否在 1 到 8 之间。
        如果任何一个条件不满足，则输出错误信息：
        -Python-
        print('Ошибка, некорректный ввод')

        3.判断两个格子是否在同一行或同一列：
        比较两个格子的字母部分（列）和数字部分（行）：
        -Python-
        if cell_1[0] == cell_2[0] or cell_1[1] == cell_2[1]:
            print('да')
        else:
            print('нет')
        如果两个格子的字母部分相同（即在同一列），或者数字部分相同（即在同一行），则输出“да”。
        否则输出“нет”。
6. **编写 whole_part和fractional_part  函数** 

        *功能：判断用户输入的两个国际象棋棋盘上的格子是否相邻。国际象棋棋盘由8×8的格子组成，每个格子用一个字母（a到h）和一个数字（1到8）表示。代码会检查输入的格子坐标是否有效，并判断这两个格子是否在水平、垂直或对角方向上相邻。

        *参数：
        -cell_1：用户输入的第一个格子的坐标，通过 input() 函数获取，存储为字符串类型。
        -cell_2：用户输入的第二个格子的坐标，通过 input() 函数获取，存储为字符串类型。

        *返回值：代码没有显式的返回值，而是直接通过 print() 函数将结果输出到控制台。

        *测试方法如下：
        1.运行代码。
        2.在提示输入时，分别输入两个格子的坐标（例如 g3 和 f2）。
        3.观察输出结果是否符合预期。

        *测试结果：
        输入 g3 和 f2，输出结果为：
        Да
        输入 c6 和 d4，输出结果为：
        Нет
        输入 a1 和 b2，输出结果为：
        Да
        输入 h8 和 g7，输出结果为：
        Да
        输入 z9 和 a1，输出结果为：
        Ошибка, некорректный ввод

        #代码解释：
        1.输入两个格子的坐标：
        cell_1 = input('Введите координаты первой клетки: ')：提示用户输入第一个格子的坐标，并将其存储为字符串。
        cell_2 = input('Введите координаты второй клетки: ')：提示用户输入第二个格子的坐标，并将其存储为字符串。

        2.检查输入的坐标是否有效：
        使用多条件判断：
        -Python-
        if ('a' <= cell_1[0] <= 'h'
                and '1' <= cell_1[1] <= '8'
                and 'a' <= cell_2[0] <= 'h'
                and '1' <= cell_2[1] <= '8'):
        检查第一个格子的字母部分是否在 a 到 h 之间。
        检查第一个格子的数字部分是否在 1 到 8 之间。
        检查第二个格子的字母部分是否在 a 到 h 之间。
        检查第二个格子的数字部分是否在 1 到 8 之间。
        如果任何一个条件不满足，则输出错误信息：
        -Python-
        print('Ошибка, некорректный ввод')

        3.判断两个格子是否相邻：
        使用条件判断：
        -Python-
        if -1 <= ord(cell_1[0]) - ord(cell_2[0]) <= 1 and -1 <= int(cell_1[1]) - int(cell_2[1]) <= 1:
        ord(cell_1[0]) - ord(cell_2[0])：计算两个格子的列坐标（字母部分）的ASCII码值之差。
        int(cell_1[1]) - int(cell_2[1])：计算两个格子的行坐标（数字部分）的差值。
        如果两个格子的列坐标差值和行坐标差值都在 -1 到 1 之间，则说明它们相邻（包括水平、垂直或对角方向）。
        如果满足上述条件，则输出“Да”；否则输出“Нет”。
<!-- by 黄家翔 -->
### Tasks and Functional Descriptions for April 9, 2023:

1. **Function: `name`**
   - **Functionality:** Retrieves the user's first name, last name, and year of birth, calculates the current age, and outputs the user's information and age in a specified format.
   - **Parameters:**
     - `name`: The user's first name, type `str`.
     - `lastname`: The user's last name, type `str`.
     - `year`: The user's year of birth, type `int`.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     ```python
     name = input('Enter your first name: ')
     lastname = input('Enter your last name: ')
     year = int(input('Enter your year of birth: '))
     print(lastname, name + ',', 2023 - year)
     ```
   - **Test Results:**
     - Input:
       ```
       Enter your first name: Liliya
       Enter your last name: Rafikova
       Enter your year of birth: 1989
       ```
       Output:
       ```
       Rafikova Liliya, 34
       ```
   - **Explanation:**
     - The `input()` function returns the user's input as a string. To convert the year to an integer, we use `int(input())`.
     - The code then prints the last name, first name, and the calculated age (2023 - year of birth).

2. **Function: `number`**
   - **Functionality:** Receives an integer input from the user and outputs the next and previous numbers.
   - **Parameters:**
     - `number`: The integer input by the user, converted to `int` using `int(input())`.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter an integer (e.g., `100`).
     3. Observe the output.
   - **Test Results:**
     - Input `100`:
       ```
       The next number for 100 is 101.
       The previous number for 100 is 99.
       ```
     - Input `-5`:
       ```
       The next number for -5 is -4.
       The previous number for -5 is -6.
       ```
     - Input `0`:
       ```
       The next number for 0 is 1.
       The previous number for 0 is -1.
       ```
   - **Explanation:**
     - The code calculates the next number by adding 1 to the input number and the previous number by subtracting 1 from the input number.

3. **Function: `minutes`**
   - **Functionality:** Converts the input minutes into hours and minutes and outputs the result.
   - **Parameters:**
     - `minutes`: The number of minutes input by the user, converted to `int` using `int(input())`.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter a number of minutes (e.g., `130`).
     3. Observe the output.
   - **Test Results:**
     - Input `130`:
       ```
       130 minutes is 2 hours 10 minutes.
       ```
     - Input `90`:
       ```
       90 minutes is 1 hour 30 minutes.
       ```
     - Input `60`:
       ```
       60 minutes is 1 hour 0 minutes.
       ```
     - Input `59`:
       ```
       59 minutes is 0 hours 59 minutes.
       ```
   - **Explanation:**
     - The code calculates the number of hours using integer division (`//`) and the remaining minutes using the modulus operator (`%`).

4. **Function: `number`**
   - **Functionality:** Receives a three-digit number, calculates the sum and product of its digits, and outputs the results.
   - **Parameters:**
     - `number`: The three-digit number input by the user, converted to `int` using `int(input())`.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter a three-digit number (e.g., `123`).
     3. Observe the output.
   - **Test Results:**
     - Input `123`:
       ```
       Sum of digits = 6
       Product of digits = 6
       ```
     - Input `456`:
       ```
       Sum of digits = 15
       Product of digits = 120
       ```
     - Input `100`:
       ```
       Sum of digits = 1
       Product of digits = 0
       ```
   - **Explanation:**
     - The code extracts the individual digits using modulus and integer division operations and then calculates their sum and product.

5. **Function: `whole_part` and `fractional_part`**
   - **Functionality:** Receives the integer and fractional parts of a number, combines them into a floating-point number (representing miles), converts it to kilometers, and outputs the result.
   - **Parameters:**
     - `whole_part`: The integer part of the number, input by the user as a string.
     - `fractional_part`: The fractional part of the number, input by the user as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter the integer and fractional parts separately (e.g., `15` for the integer part and `7` for the fractional part).
     3. Observe the output.
   - **Test Results:**
     - Input integer part `15`, fractional part `7`:
       ```
       15.7 miles = 25.3 km
       ```
     - Input integer part `10`, fractional part `5`:
       ```
       10.5 miles = 16.9 km
       ```
     - Input integer part `0`, fractional part `5`:
       ```
       0.5 miles = 0.8 km
       ```
   - **Explanation:**
     - The code combines the integer and fractional parts into a floating-point number and then converts it to kilometers using the conversion factor (1 mile = 1.61 km).

### Tasks and Functional Descriptions for April 16, 2023:

1. **Function: `num_1`, `num_2`, `num_3`, and `summa_positiv`**
   - **Functionality:** Receives three numbers from the user, determines if they are positive (including positive integers and decimals), sums all positive numbers, and outputs the total.
   - **Parameters:**
     - `num_1`: The first number input by the user, stored as a string.
     - `num_2`: The second number input by the user, stored as a string.
     - `num_3`: The third number input by the user, stored as a string.
     - `summa_positiv`: A variable to store the sum of positive numbers, initialized to `0`.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter three numbers (positive, negative, or decimal).
     3. Observe the output.
   - **Test Results:**
     - Input `-23`, `2.3`, `1`:
       ```
       3.3
       ```
     - Input `-1`, `-2`, `-3`:
       ```
       0.0
       ```
     - Input `0`, `5`, `10.5`:
       ```
       15.5
       ```
     - Input `12.3`, `45.6`, `78.9`:
       ```
       136.8
       ```
   - **Explanation:**
     - The code checks if each number is positive by removing the decimal point (if present) and verifying if the remaining string consists only of digits. Positive numbers are converted to floats and added to the sum.

2. **Function: `num_1` and `num_2`**
   - **Functionality:** Receives two integers from the user, determines if the first number is divisible by the second, and outputs the result. If the second number is zero, it outputs an error message. The code also checks if the inputs are valid integers.
   - **Parameters:**
     - `num_1`: The first number input by the user, stored as a string.
     - `num_2`: The second number input by the user, stored as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter two numbers (integers or non-integers).
     3. Observe the output.
   - **Test Results:**
     - Input `25` and `3`:
       ```
       25 не делится на 3 нацело
       неполное частное: 8
       остаток: 1
       ```
     - Input `8` and `2`:
       ```
       8 делится на 2 нацело
       частное: 4
       ```
     - Input `2` and `0`:
       ```
       Ошибка, на ноль делить нельзя
       ```
     - Input `abc` and `2`:
       ```
       Ошибка, некорректный ввод
       ```
   - **Explanation:**
     - The code converts the inputs to integers and checks if the second number is zero. If not, it calculates the quotient and remainder to determine divisibility.

3. **Function: `year`**
   - **Functionality:** Determines if the input year is a leap year. If it is, it outputs "да"; otherwise, it outputs "нет". The code also checks if the input is a valid integer.
   - **Parameters:**
     - `year`: The year input by the user, initially stored as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter a year (integer or non-integer).
     3. Observe the output.
   - **Test Results:**
     - Input `2020`:
       ```
       да
       ```
     - Input `2023`:
       ```
       нет
       ```
     - Input `1900`:
       ```
       нет
       ```
     - Input `2000`:
       ```
       да
       ```
     - Input `abc`:
       ```
       Ошибка, некорректный ввод
       ```
   - **Explanation:**
     - The code converts the input to an integer and checks the leap year conditions: divisible by 4 but not by 100, or divisible by 400.

4. **Function: `cell_1` and `cell_2`**
   - **Functionality:** Determines if two chessboard squares (input as coordinates) are of the same color. The code checks if the inputs are valid coordinates and then compares the colors of the squares.
   - **Parameters:**
     - `cell_1`: The coordinates of the first square, input by the user as a string.
     - `cell_2`: The coordinates of the second square, input by the user as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter two sets of coordinates (e.g., `a1` and `b2`).
     3. Observe the output.
   - **Test Results:**
     - Input `a1` and `b2`:
       ```
       да
       ```
     - Input `a1` and `a2`:
       ```
       нет
       ```
     - Input `h8` and `a1`:
       ```
       нет
       ```
     - Input `e5` and `e4`:
       ```
       да
       ```
     - Input `z9` and `a1`:
       ```
       Ошибка, некорректный ввод
       ```
   - **Explanation:**
     - The code calculates the sum of the ASCII values of the letters and the numeric values of the coordinates. If the parity (even or odd) of these sums is the same for both squares, they are of the same color.

5. **Function: `cell_1` and `cell_2`**
   - **Functionality:** Determines if two chessboard squares are in the same row or column. The code checks if the inputs are valid coordinates and then compares the rows and columns.
   - **Parameters:**
     - `cell_1`: The coordinates of the first square, input by the user as a string.
     - `cell_2`: The coordinates of the second square, input by the user as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter two sets of coordinates (e.g., `d4` and `e4`).
     3. Observe the output.
   - **Test Results:**
     - Input `d4` and `e4`:
       ```
       да
       ```
     - Input `a2` and `c4`:
       ```
       нет
       ```
     - Input `a1` and `a8`:
       ```
       да
       ```
     - Input `h8` and `a1`:
       ```
       нет
       ```
     - Input `z9` and `a1`:
       ```
       Ошибка, некорректный ввод
       ```
   - **Explanation:**
     - The code compares the letters (columns) and numbers (rows) of the coordinates. If either the columns or rows match, the squares are in the same row or column.

6. **Function: `cell_1` and `cell_2`**
   - **Functionality:** Determines if two chessboard squares are adjacent (horizontally, vertically, or diagonally). The code checks if the inputs are valid coordinates and then calculates the differences in rows and columns.
   - **Parameters:**
     - `cell_1`: The coordinates of the first square, input by the user as a string.
     - `cell_2`: The coordinates of the second square, input by the user as a string.
   - **Return Value:** No explicit return value. The result is printed directly using the `print` function.
   - **Testing Method:**
     1. Run the code.
     2. Enter two sets of coordinates (e.g., `g3` and `f2`).
     3. Observe the output.
   - **Test Results:**
     - Input `g3` and `f2`:
       ```
       Да
       ```
     - Input `c6` and `d4`:
       ```
       Нет
       ```
     - Input `a1` and `b2`:
       ```
       Да
       ```
     - Input `h8` and `g7`:
       ```
       Да
       ```
     - Input `z9` and `a1`:
       ```
       Ошибка, некорректный ввод
       ```
   - **Explanation:**
     - The code calculates the differences in ASCII values of the letters and the numeric values of the coordinates. If both differences are within -1 to 1, the squares are adjacent.