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

## 📮 Project Main Function Description and Screenshots
<!-- by 钟章鸿 -->
### Tasks and Instructions for 2023.07.02 Files

1. Implement the Tetrahedron Class

    Functionality:
        Describes the geometric properties of a regular tetrahedron (all faces are equilateral triangles) and provides methods to calculate its surface area and volume.
    Parameters:
        Parameter 1: Side length, type: float.
    Methods:
        surface():
            Function: Calculates the surface area of the tetrahedron. Returns a float.
        volume():
            Function: Calculates the volume of the tetrahedron. Returns a float.
    Test Method & Result:
        ![alt text](./asset/2023.07.02/image-1.png)

2. Implement the PowerMeter Class
    Functionality:
        Simulates a dual-tariff electricity meter (i.e., different unit prices depending on the time period).
    Parameters:
        tariff1: Unit price for rate 1 (default: 4.35).
        tariff2: Unit price for rate 2 (default: 3.21).
        tariff2_starts: Start time of rate 2 (default: 23:00).
        tariff2_ends: End time of rate 2 (default: 07:00).
    Methods:
        __repr__():
            Function: Returns the string representation of the power meter, showing the accumulated electricity usage (in kWh).
        __str__():
            Function: Returns the string representation of the power meter, showing the current month's and today's accumulated electricity cost.
        meter(power):
            Function: Accepts a usage value (power), calculates the corresponding electricity cost, updates the meter's status, and returns the cost of this usage (type: Decimal).
    Test Method:
        ```python
            pm1 = PowerMeter()
            pm1.meter(5)
        ```
    Test Result:
        ![alt text](./asset/2023.07.02/image-2.png)

3. Implement the ChessKing Class

    Functionality:
        Describes the behavior and rules of the King piece in international chess.

    Methods:

        __repr__():
            Function: Returns the string representation of the King piece, used for debugging.

        __str__():
            Function: Returns the string representation of the King piece, used for printing.

        is_turn_valid(new_square):
            Function: Checks whether a move from the current square to the new square is valid for a King. Returns True if the move is legal, False otherwise.

        turn(new_square):
            Function: Performs the move from the current square to the target square.

    Test Method & Result:
        ![alt text](./asset/2023.07.02/image-3.png)

4. Implement the CountableNouns Class

    Functionality:
        Handles the grammatical changes of countable nouns in Russian based on numeric context. In Russian, noun forms change depending on the number.

    Methods:

        pick(number, word):
            Function: Based on the input number and base form of the noun, returns the correct noun form.

        save_words(word1):
            Function: Through interactive input, adds new noun forms to the internal words dictionary and words.csv file. If word1 is not provided, prompts the user for input.

    Test Method & Result:
        ![alt text](./asset/2023.07.02/image-4.png)

### Tasks, Functions, and Usage under the Folder 2023.07.30:
1. Implement the Point, Line, and Polygon Classes

    Point Class

        Functionality:

            Stores coordinates of a point (x and y).

            Provides read-only attributes.

            Supports comparison and string representation.

        Parameters:

            x: float, y: float

        Methods:

            __eq__(): Compares two points (equal if both x and y are equal).

            __str__() and __repr__(): Returns the string representation of the point.

    Line Class

        Functionality:
             a line segment defined by two points (start and end), supports length calculation and dynamic updating of endpoints.

        Parameters:

            start: Point

            end: Point

        Methods:

            length_calc(): Calculates the distance between the two points (i.e., the length of the line segment).

            start(), end(): Endpoints can be dynamically updated but must be assigned as Point objects; otherwise, a TypeError is raised.

            __str__() and __repr__(): Returns the string representation of the line.

    Polygon Class

        Functionality:
            Represents a polygon composed of multiple line segments. Supports checking whether the polygon is closed and calculating its perimeter.

        Methods:

            is_closed():
                Function: 
                    Checks whether the polygon is closed:
                    Whether the first and last segments are connected.
                    Whether each segment’s endpoint connects to the next segment’s start point.

            perimeter():
                Function: 
                    Calculates the total perimeter (sum of all segment lengths).
                    If the polygon is not closed, raises a ValueError.

    Test Method & Result:
        ![alt text](./asset/2023.07.30/image-1.png)
<!-- by 钟章鸿 -->



