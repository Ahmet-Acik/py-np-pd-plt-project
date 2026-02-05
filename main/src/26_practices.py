"""
Python Practices File

This file contains various Python code examples and practices covering:
- Sets and their operations
- Dictionaries and their methods
- List comprehensions and comprehensions for other data types
- Functions, lambdas, map, filter
- Error handling and logging
- File I/O with text and JSON files
- Tuples and sequences (Fibonacci, primes, etc.)

Each section demonstrates best practices in Python coding.
"""

# Section 1: Sets
print("=== Sets Practices ===")

# Creating sets
my_set = {1, 2, 3, 4, 5}
my_empty_set = set()  # Note: {} creates a dict, not set
print(f"my_set: {my_set}")
print(f"my_empty_set: {my_empty_set}")

# Sets are unordered, unindexed, and do not allow duplicates
# Set methods: add, copy, remove, discard, pop, clear, update
my_set.add(6)
print(f"my_set after adding 6: {my_set}")

copied_set = my_set.copy()
print(f"copied_set: {copied_set}")

my_set.discard(6)  # Safe removal, no error if not found
print(f"my_set after discarding 6: {my_set}")

item = my_set.pop()  # Removes and returns arbitrary element
print(f"my_set after popping: {my_set}, popped item: {item}")

try:
    my_set.remove(10)  # Raises KeyError if not found
except KeyError as e:
    print(f"Error removing 10: {e}")

# Updating sets
my_set2 = {0, 2, 3, 4, 5}
my_set2.update({6, 7, 8}, [9, 10], (11, 12))  # Add multiple iterables
print(f"my_set2 after update: {my_set2}")

# Section 2: Dictionaries
print("\n=== Dictionaries Practices ===")

# Creating dictionaries
character = {
    "name": "Ahmet",
    "age": 25,
    "weight": 72.5,
    "is_student": True,
}
print(f"character dict: {character}")

# Accessing values
print(f"Name: {character['name']}")
print(f"Age: {character.get('age')}")
print(f"Height (default): {character.get('height', 'not found')}")

# Adding/updating
character["height"] = 175  # Corrected: single value, not tuple
character["age"] = 26
print(f"Updated character: {character}")

# Dictionary methods
print(f"Keys: {list(character.keys())}")
print(f"Values: {list(character.values())}")
print(f"Items: {list(character.items())}")

# Iterating
for key, value in character.items():
    print(f"{key}: {value}")

# Creating dicts from other structures
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(f"Dict from zip: {my_dict}")

new_dict = dict.fromkeys(['x', 'y', 'z'], 0)
print(f"Dict from keys: {new_dict}")

# Section 3: Comprehensions
print("\n=== Comprehensions Practices ===")

# List comprehensions
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Flattened list: {flattened}")

even_numbers = [x for sublist in nested_list for x in sublist if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Dictionary comprehensions
square_dict = {x: x**2 for x in range(6)}
print(f"Square dict: {square_dict}")

prices = {"apple": 1, "banana": 2, "orange": 3}
double_prices = {key: value * 2 for key, value in prices.items()}
print(f"Double prices: {double_prices}")

# Set comprehensions
square_set = {x**2 for x in range(6) if x > 3}
print(f"Square set: {square_set}")

# Generator expressions (for tuples)
square_tuple = tuple(x**2 for x in range(7) if x % 2 == 0)
print(f"Square tuple: {square_tuple}")

# Section 4: Functions, Lambdas, Map, Filter
print("\n=== Functions and Functional Programming Practices ===")

# Functions
def greet(name: str, age: int) -> str:
    """Greet a person with name and age."""
    return f"Hello, {name}, you are {age} years old!"

print(greet("Ahmet", 25))

def add_item_to_list(item, lst=None):
    """Add item to list, using None as default to avoid mutable default arg."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_to_list(5))
print(add_item_to_list(10))

# Lambdas
add = lambda x, y: x + y
print(f"Lambda add: {add(2, 3)}")

# Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# Filter
fruits = ["apple", "banana", "cherry", "mango", "melon", "orange"]
fruits_with_m = list(filter(lambda x: x.startswith("m"), fruits))
print(f"Fruits starting with 'm': {fruits_with_m}")

# Section 5: Error Handling and Logging
print("\n=== Error Handling and Logging Practices ===")

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def process_data(data):
    """Process data with proper error handling and logging."""
    logging.debug("Processing data: %s", data)
    if not data:
        logging.warning("No data provided")
        raise ValueError("Data cannot be empty")

    try:
        if len(data) < 2:
            raise ValueError("Data must contain at least two elements")
        result = data[0] / data[1]
        logging.info("Calculation result: %s", result)
        return result
    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError: %s", e)
        return None
    except TypeError as e:
        logging.error("TypeError: %s", e)
        return None
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        return None
    finally:
        logging.info("Data processing complete")

print(f"process_data([10, 5]): {process_data([10, 5])}")
print(f"process_data([10, 0]): {process_data([10, 0])}")
try:
    print(f"process_data([]): {process_data([])}")
except ValueError as e:
    print(f"Caught expected error: {e}")

# Section 6: File I/O
print("\n=== File I/O Practices ===")

import os
import json

# Text file
text_file_path = 'flt.txt'
if not os.path.exists(text_file_path):
    with open(text_file_path, 'w') as file:
        file.write('1,2,3\n4,5,6\n7,8,9\n')

nested_list = []
with open(text_file_path, 'r') as file:
    for line in file:
        nested_list.append([int(num) for num in line.strip().split(',')])

flattened_filtered = [num for sublist in nested_list for num in sublist if num > 3 and num % 2 != 0]
print(f"Filtered flattened from text: {flattened_filtered}")

# JSON file
json_file_path = 'flt.json'
if not os.path.exists(json_file_path):
    sample_data = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 75},
        {"name": "Charlie", "grade": 90},
    ]
    with open(json_file_path, 'w') as file:
        json.dump(sample_data, file, indent=4)

with open(json_file_path, 'r') as file:
    students = json.load(file)

high_scorers = [student["name"] for student in students if student["grade"] > 80]
print(f"High scorers: {high_scorers}")

# Section 7: Tuples and Sequences
print("\n=== Tuples and Sequences Practices ===")

# Fibonacci series using while loop
a, b = 0, 1
while b < 100:
    print(b, end=", ")
    a, b = b, a + b
print()

# Fibonacci series using for loop
a, b = 0, 1
for i in range(10):
    print(b, end=", ")
    a, b = b, a + b
print()

# Fibonacci generator function
def fibonacci(n: int):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_tuple = tuple(fibonacci(10))
print(f"Fibonacci tuple: {fibonacci_tuple}")

# Tuple comprehensions (using generator expressions)
strings = ["apple", "banana", "cherry"]
uppercase_tuple = tuple(s.upper() for s in strings)
print(f"Uppercase tuple: {uppercase_tuple}")

squared_tuple = tuple((n, n ** 2) for n in range(1, 9))
print(f"Squared pairs: {squared_tuple}")

strings_nums = ["1", "2", "3", "4", "5"]
numbers_tuple = tuple(int(s) for s in strings_nums)
print(f"Numbers tuple: {numbers_tuple}")

# Prime numbers
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_tuple = tuple(n for n in range(20) if is_prime(n))
print(f"Primes less than 20: {primes_tuple}")

# Other tuple examples
reversed_tuple = tuple(s[::-1] for s in strings)
print(f"Reversed strings: {reversed_tuple}")

squares_divisible_by_3 = tuple(x**2 for x in range(1, 31) if x % 3 == 0)
print(f"Squares divisible by 3: {squares_divisible_by_3}")

sentence = "Python is a powerful programming language"
word_lengths = tuple(len(word) for word in sentence.split())
print(f"Word lengths: {word_lengths}")

text = "Hello"
ascii_tuple = tuple(ord(char) for char in text)
print(f"ASCII values: {ascii_tuple}")

binary_representation = tuple((x, bin(x)) for x in range(1, 6))
print(f"Binary representations: {binary_representation}")

print("\n=== End of Practices ===")