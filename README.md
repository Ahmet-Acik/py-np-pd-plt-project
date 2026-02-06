# Python Data Science Tutorial

A comprehensive Python tutorial covering fundamental programming concepts to advanced data science topics. This project includes interactive examples and exercises to help you learn Python step by step.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each Python file in the `main/src/` directory demonstrates a specific concept. Run them individually to see examples:

```bash
python main/src/01_hello.py
python main/src/02_variable.py
# etc.
```

Or run from within the `main/src/` directory:
```bash
cd main/src
python 01_hello.py
```

## Project Structure

```
python-data-science-tutorial/
├── requirements.txt          # Python dependencies
├── data/                     # Data files for examples
├── main/
│   └── src/                  # Tutorial Python files
│       ├── 01_hello.py       # Print statements and basic output
│       ├── 02_variable.py    # Variable assignment and types
│       ├── 03_strings.py     # String operations and methods
│       ├── 04_lists.py       # List data structure
│       ├── 05_tuples.py      # Tuple data structure
│       ├── 06_sets.py        # Set data structure
│       ├── 07_dictionaries.py # Dictionary data structure
│       ├── 08_conditionals.py # If-else statements
│       ├── 09_loops.py       # For and while loops
│       ├── 10_loops_nested_comprehensions.py # Advanced loops
│       ├── 11_functions.py   # Function definitions
│       ├── 12_functions_8.py # More functions
│       ├── 13_comprehension.py # List comprehensions
│       ├── 14_comprehensions_and_generator.py # Generators
│       ├── 15_oop.py         # Object-oriented programming basics
│       ├── 16_oop2.py        # OOP continued
│       ├── 17_oop3.py        # Advanced OOP
│       ├── 18_classes.py     # Class definitions
│       ├── 19_error_handles.py # Error handling
│       ├── 20_logging_practices.py # Logging
│       ├── 21_Io_read_write.py # File I/O
│       ├── 24_numpys.py      # NumPy introduction
│       ├── 25_pandas_intro.py # Pandas introduction
│       ├── 26_practices.py   # Practice exercises
│       ├── 27_main_example_script.py # Example script
│       ├── 28_main_example_modified_script # Modified example
│       ├── 29_variable_se.py # Variable scope
│       ├── 30_matplotlib_intro.py # Matplotlib plotting
│       └── ...               # Additional files
├── notebooks/                # Jupyter notebooks
└── tests/                    # Test files
```

## Data Files

Sample datasets are provided in the `data/` directory for use in Pandas and data analysis examples:

- `sample_data.csv`: A simple CSV file with employee data (name, age, city, salary) for basic data manipulation exercises.

## Tutorial Files Overview

The files are numbered sequentially for a progressive learning experience:

1. **01_hello.py**: Introduction to print statements and basic output
2. **02_variable.py**: Variable declaration, assignment, and data types
3. **03_strings.py**: String manipulation, methods, and operations
4. **04_lists.py**: List creation, indexing, and methods
5. **05_tuples.py**: Tuple data structure and immutability
6. **06_sets.py**: Set operations and methods
7. **07_dictionaries.py**: Dictionary creation and manipulation
8. **08_conditionals.py**: Conditional statements (if/elif/else)
9. **09_loops.py**: Loop structures (for/while)
10. **10_loops_nested_comprehensions.py**: Nested loops and comprehensions
11-12. **Functions**: Function definition and advanced concepts
13-14. **Comprehensions & Generators**: List comprehensions and generators
15-18. **OOP**: Object-oriented programming concepts
19. **Error Handling**: Try/except blocks and error management
20. **Logging**: Logging practices and configuration
21. **File I/O**: Reading and writing files
24. **NumPy**: Introduction to numerical computing
25. **Pandas**: Data manipulation and analysis
26-30. **Practice & Examples**: Exercises and real-world examples

## Contributing

Feel free to contribute by:
- Adding more examples
- Improving existing code
- Fixing bugs
- Adding documentation

## License

This project is for educational purposes. Feel free to use and modify as needed.