# Python example of binary representation
number = 13
binary_representation = bin(number)  # Converts to binary
print(binary_representation)  # Output: '0b1101'

# ASCII representation
character = 'A'
ascii_value = ord(character)  # Converts to ASCII
print(ascii_value)  # Output: 65

import os
# Hexadecimal representation
hex_number = hex(number)  # Converts to hexadecimal
print(hex_number)  # Output: '0xd'

# Inefficient representation: Using float for integers
numbers = [1.0, 2.0, 3.0]  # Consumes more memory and slows down operations

# Efficient representation: Using integers
numbers2 = [1, 2, 3]  # Faster and uses less memory

# Binary operations for performance
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x & y  # Bitwise AND is faster than arithmetic operations
print(result)  # Output: 1

# Octal representation
octal_number = oct(number)  # Converts to octal
print(octal_number)  # Output: '0o15'

# Binary representation of a number
binary_number = bin(255)  # Converts to binary
print(binary_number)  # Output: '0b11111111'