# Python Utilities and Learning Toolkit

## Description

This project is a comprehensive collection of Python scripts and utility modules designed for both learning and practical use. It covers a wide range of topics, including file and directory operations, terminal message formatting, dynamic module importing, text search with context extraction, function call logging, and SI unit conversion. The project provides both main implementations and reference versions (`*_ref.py`) for comparative study and deeper understanding of different programming approaches.

The `data` directory contains various supporting files, such as quiz question banks, configuration files, historical texts, images, and archives, enabling batch text processing, configuration management, and logging.

## Features

- **File and Directory Operations**: Quickly list all files in a directory for management and batch processing.
- **Terminal Message Formatting**: Beautify and center important messages for enhanced terminal interaction.
- **Dynamic Module Importing**: Load external Python files or configuration files at runtime for flexible program behavior.
- **Text Search with Context Extraction**: Search for keywords in multiple text files and extract surrounding context for analysis.
- **Function Call Logging**: Automatically log function calls, parameters, return values, and exceptions for debugging and tracing.
- **SI Unit Conversion**: Convert numbers to appropriate SI prefixes for scientific computing and display.
- **Data and Configuration Management**: Use files like `vars.py` and `conf.py` for quiz constants and application settings.

## Installation

1. **Clone or download** this repository, ensuring the `data` directory and its contents are intact.
2. Make sure you have Python 3.10 or higher installed.

## Usage

This project consists of several independent Python scripts, each demonstrating a specific utility or programming technique. You can run each script directly from the command line, or import and use the utility functions in your own code.

### 1. List Files in a Directory

- **Script:** `1.py` or `1_ref.py`
- **How to use:**
  ```python
  from 1 import list_files
  print(list_files(r'./data'))
  # Output: ('7MD9i.chm', 'conf.py', 'E3ln1.txt', ...)
  ```
  Or run interactively:
  ```bash
  python -i 1.py
  >>> list_files(r'./data')
  ```

### 2. Beautify and Print Important Messages

- **Script:** `2.py` or `2_ref.py`
- **How to use:**
  ```bash
  python 2.py
  ```
  The script will prompt you to enter a message, then print it in a decorated, centered box in the terminal.
  Example:
  ```
   Введите текст: PROGRAM TITLE

   #==============================#
   #                              #
   #        PROGRAM TITLE         #
   #                              #
   #==============================#
  ```

- **Direct function usage:**
  ```python
  from utils import important_message
  print(important_message('Hello World!'))
  ```

### 3. Dynamically Import a File

- **Script:** `3.py` or `3_ref.py`
- **How to use:**
  ```bash
  python 3.py
  ```
  The script will prompt for a file path. Enter the path to a Python file (e.g., `./data/conf.py`). If the file exists, it will be copied and imported as a module.

### 4. Search for Keywords in Text Files

- **Script:** `4.py` or `4_ref.py`
- **How to use:**
  ```python
  from 4 import search_context
  results = search_context('keyword', 'another', context=1)
  for item in results:
      print(item)
  ```
  - Searches all `.txt` files in the `data` directory for lines containing the given keywords.
  - Returns a list of dictionaries with filename, line number, context, and matched text.

### 5. Function Call Logging

- **Script:** `5.py` or `5_ref.py`
- **How to use:**
  ```python
  from 5 import logger
  @logger
  def add(a, b):
      return a + b

  add(1, 2)
  # Each call is logged to data/function_calls.log
  ```

### 6. SI Unit Conversion

- **Script:** `si_unit.py`
- **How to use:**
  ```python
  from si_unit import SIUnit
  v = SIUnit(1500, 'm')
  print(v)           # Output: 1.5 km
  print(v.target(0)) # Output: 1500 m
  ```

### Notes

- Some scripts require user input in the terminal.
- Some scripts depend on files in the `data` directory (e.g., `conf.py`, `.txt` files).
- All utility functions can be imported and reused in your own Python projects.

## Requirements or Dependencies

- **Python Version**: 3.10 or higher recommended.
- **Dependencies**: Only Python standard library modules are used (e.g., `pathlib`, `shutil`, `importlib`, `sys`, `datetime`). No third-party packages required.

## File Structure

```
2023.05.28/
│
├── 1.py, 1_ref.py           # List files in a directory
├── 2.py, 2_ref.py           # Beautify and print important messages
├── 3.py, 3_ref.py           # Prompt for file path and dynamically import modules
├── 4.py, 4_ref.py           # Search for keywords in text files with context
├── 5.py, 5_ref.py           # Function call logging decorators
├── si_unit.py               # SI unit conversion and formatting
├── utils.py, utils_ref.py   # Utility functions (message formatting, dynamic import, etc.)
├── 20230528-markdown.md     # Detailed documentation (in Chinese)
├── # HW 2023.05.28.txt      # Assignment and usage instructions (in Russian)
│
└── data/
    ├── vars.py              # Constants and settings for the quiz game
    ├── conf.py              # Example configuration dictionary
    ├── questions.quiz       # Quiz question bank
    ├── *.txt                # Text files for search and analysis
    ├── function_calls.log   # Log file for function calls
    ├── *.chm, *.docx, *.jpg, *.zip # Miscellaneous data files
    ├── c14KE/, mXbd9/       # Subdirectories with additional data files
    └── __pycache__/         # Python cache files (auto-generated)
```

## License

This project is intended for educational and practical use. Please refer to the repository or contact the author for licensing details. 