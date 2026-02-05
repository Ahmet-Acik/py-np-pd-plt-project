"""
Variables Examples

This file demonstrates basic variable declaration, assignment, and operations in Python.
Following best practices for naming, types, and usage.
"""

# Basic variable declarations
name: str = "Ahmet"
age: int = 25
height: float = 175.5
is_student: bool = True

# Printing variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Is student: {is_student}")

# Variable operations
next_year_age = age + 1
print(f"Age next year: {next_year_age}")

# Type checking
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Constants (by convention, uppercase)
PI = 3.14159
GRAVITY = 9.81
print(f"PI: {PI}, Gravity: {GRAVITY}")

# Variable reassignment
age = 26  # Reassigning is allowed
print(f"Updated age: {age}")

if __name__ == "__main__":
    print("Variables examples completed.")