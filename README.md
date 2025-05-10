# Top-Python321
---

This is a collection of Python basic usage assignments where the teacher has arranged Python exercises for students, covering topics such as input/output operations, variables and data types, formatted output, conditional statements, loops, file handling and module imports, and function writing.

## ✨ Project Features

- 📝 Practice-Oriented  
    All tasks require students to write code themselves. This hands-on approach helps deepen their understanding and application of the Python programming language, effectively enhancing their coding skills.
- ✅ Gradual Difficulty Increase  
    Tasks start with basic input/output operations and variables, then progress to conditional statements and loops, and finally move on to function definitions, file operations, etc. This forms a learning path that gradually increases in difficulty.
- 💾 Comprehensive Knowledge Coverage  
    It covers many important aspects of Python programming, including but not limited to data types, control structures, functions, modules, file operations, exception handling, etc. This enables students to gain a comprehensive understanding and mastery of the Python programming language.
- 🎨 Feedback and Evaluation Mechanism  
    Students are asked to keep the output results of their code in the form of comments in the code files and report their assignment completion status in the designated "Журнал" service. This helps teachers evaluate and provide feedback on students' learning progress and outcomes.
- 🔑 Combined with Practical Applications  
    The tasks involve scenarios such as password strength checking, taxi fare calculation, and file operations, which are related to real-life or work situations. This enables students to apply their knowledge to practical problems.

## 🚀 Quick Start

### Clone the Project

```bash
git clone https://github.com/Glccccc/wuyanzu-group.git
cd wuyanzu-group
```

### Launch the Project
```bash  
cd wuyanzu-group/2023.04.09
python 1.py
python 2.py
...
```
The project will run in your local ```development environment```.
## 📦 Project Structure
```
wuyanzu-group/
├── 2023.04.09/
│   ├── # HW 2023.04.09.txt
│   ├── 1.py
│   ├── 2.py
│   ├── 3.py
│   ├── 4.py
│   └── 5.py
├── 2023.04.16/
├── 2023.04.23/
├── ...
└── README.md
```
## 📮 Project Main Function Description and Screenshots
<!-- by 管立超 -->
### Tasks and Instructions for 2023.05.14 Files

1. **Implement the strong_password Function**
    
    *Function:* Checks if a password is strong.
    
    *Parameters:*
    - Parameter 1: A required keyword parameter of type str representing the password.
    
    *Return Value:*
    - A bool. Returns True if the password meets the following conditions, otherwise False:
        - Minimum length of 8 characters.
        - Contains both uppercase and lowercase Latin letters.
        - Contains at least two numeric characters.
        - Contains at least one non-alphanumeric character.
    
    *Testing Method:*
    ```python
    strong_password('aA1!') == False  # Insufficient length
    strong_password('aA1!aA1!') == True  # Meets all conditions
    ```
    
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-2.png)

2. **Implement the taxi_cost Function**
    
    *Function:* Calculates the taxi fare.
    
    *Parameters:*
    - Parameter 1: A required keyword parameter of type int representing the trip distance in meters.
    - Parameter 2: An optional keyword parameter of type int representing waiting time in minutes, defaulting to 0.
    
    *Return Value:*
    - Returns None if parameters are invalid (e.g., negative values).
    - Otherwise, calculates and returns the fare (as an integer) based on the rules:
        - Base fare is 80 rubles.
        - 6 rubles for every 150 meters.
        - 3 rubles for every minute of waiting.
        - If the trip distance is 0 meters (cancellation), a penalty of 80 rubles plus waiting time cost is added.
        - The final cost is mathematically rounded to the nearest integer.
    
    *Testing Method:*
    ```python
    taxi_cost(1500)
    ```
    
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-3.png)

3. **Implement the numbers_strip Function**
    
    *Function:* Removes the n smallest and largest numbers from a list.
    
    *Parameters:*
    - Parameter 1: A required positional-keyword parameter, a list of floats.
    - Parameter 2: An optional positional-keyword parameter n, defaulting to 1, of type int.
    - Parameter 3: A strict keyword parameter of type bool, defaulting to False, to decide whether to return the modified original list or a new list.
    
    *Return Value:*
    - Returns the modified original list or a new list based on the requirements.
    
    *Testing Method:*
    ```python
    nums = [10, 20, 30, 40, 50, 60, 70]
    nums_test = numbers_strip(nums, 3, copy=True)
    nums_test
    ```
    
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-4.png)

4. **Implement the countable_nouns Function**
    
    *Function:* Selects the appropriate Russian noun form based on the numeral.
    
    *Parameters:*
    - Parameter 1: A required parameter of type int representing the numeral.
    - Parameter 2: A required tuple parameter containing three str elements corresponding to the three forms of the noun.
    
    *Return Value:*
    - Returns the corresponding noun form based on the numeral rules.
    
    *Testing Method:*
    ```python
    countable_nouns(1, ("год", "года", "лет"))
    ```
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-5.png)

5. **Implement the central_tendency Function**
    
    *Function:* Calculates the measures of central tendency for a set of numbers.
    
    *Parameters:*
    - Parameter 1: Positional parameter 1 of type float.
    - Parameter 2: Positional parameter 2 of type float.
    - Parameter 3: Variable number of positional parameters of type float.
    
    *Return Value:*
    - A dictionary containing the following key-value pairs:
        - 'median': Median (float).
        - 'arithmetic': Arithmetic mean (float).
        - 'geometric': Geometric mean (float).
        - 'harmonic': Harmonic mean (float).
    
    *Testing Method:*
    ```python
    central_tendency(1, 2, 3, 4)
    ```
    
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-6.png)

6. **Implement the orth_triangle Function**
    
    *Function:* Calculates the third side of a right-angled triangle.
    
    *Parameters:*
    - Parameter 1: Side length of type int or float.
    - Parameter 2: Side length of type int or float.
    - Parameter 3: Hypotenuse of type int or float.  
    
    *Return Value:*
    - Returns the length of the third side (float) if the calculation is possible.
    - Returns None if the parameters are invalid.
    
    *Testing Method:*
    ```python
    orth_triangle(cath1=3, cath2=4)
    ```
    
    *Test Results:*  
    ![alt text](./asset/2023.05.14/image-7.png)

### Tasks and Instructions for 2023.05.21 Files


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
     <!-- by huangjiaxaing -->