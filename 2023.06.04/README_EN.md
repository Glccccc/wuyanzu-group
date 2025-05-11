# Recursive Algorithms and Data Processing Utilities

## Description
This project is a collection of Python scripts and data files designed for practicing and demonstrating recursive algorithms and data structure processing. The main focus is on recursive operations over nested data (such as lists, dictionaries, and trees), as well as utilities for generating and analyzing structured data, including random tree generation and batch name processing.

## Features
- Recursive calculation of the product of all numbers in arbitrarily nested iterables (lists, dictionaries, tuples, etc.)
- Recursive counting of leaf nodes in arbitrarily nested tree-like lists
- Recursive generation of random tree structures with variable depth and branching
- Utilities for batch processing and generation of names and personal data (using provided `.txt` files)
- All scripts use only the Python standard library (no third-party dependencies)

## Installation
1. Ensure you have Python 3.8 or higher installed on your system.
2. Clone or download this repository to your local machine.
3. No additional installation steps are required, as all scripts use only the standard library.

## Usage
### 1. Recursive Product Calculation (`1.1.py`)
Calculates the product of all numbers in any nested iterable structure.

**Example:**
```python
from 1.1 import product

print(product([1, 2, 3]))  # 6.0
print(product({'a': 2, 'b': [3, 4]}))  # 24.0
print(product([10, 2, [1.5, [10, 2]]]))  # 600.0
```

### 2. Tree Leaf Counting (`1.2.py`)
Counts the number of leaf nodes (non-list elements) in any nested list (tree structure).

**Example:**
```python
from 1.2 import tree_leaves

tree = [[['leaf', 'leaf'], 'leaf'], 'leaf']
print(tree_leaves(tree))  # 4
```

### 3. Random Tree Generation (`1.3.py`)
Recursively generates a random tree structure (nested lists) with 'leaf' as the leaf node.

**Example:**
```python
from 1.3 import tree_generator

tree = tree_generator()
print(tree)
```

### 4. Name and Data Batch Processing
The `.txt` files (`женские_имена.txt`, `мужские_имена_отчества.txt`, `фамилии.txt`) contain lists of Russian female names, male names with patronymics, and surnames, respectively. These can be used for batch data generation or analysis in your own scripts.

## Requirements / Dependencies
- Python 3.8+
- No third-party packages required (standard library only)

## File Structure
```
2023.06.04/
├── 1.1.py                  # Recursive product calculation
├── 1.2.py                  # Recursive tree leaf counting
├── 1.3.py                  # Random tree structure generator
├── женские_имена.txt       # Russian female names
├── мужские_имена_отчества.txt # Russian male names and patronymics
├── фамилии.txt             # Russian surnames
├── 2023.06.04_readme.md    # Original project readme (in Chinese)
├── # HW 2023.06.04_1.txt   # Homework/task description 1
├── # HW 2023.06.04_2.txt   # Homework/task description 2
├── # HW 2023.06.04_3.txt   # Homework/task description 3
├── 3.1.png                 # Screenshot or image file
```

---

For more details, see the comments and docstrings in each script, and refer to the original Chinese readme for further explanations. 