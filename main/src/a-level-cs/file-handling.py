# File handling example

# Write to a file
with open('numbers.txt', 'w') as f:
    for number in [1, 2, 3, 4, 5]:
        f.write(f"{number}\n")

# Read from a file
with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

print("Numbers read from file:", numbers)