
# range() function
rng = range(6)
print(rng)
print(list(rng))

rng = range(1, 6, 2)
print(rng)
print(list(rng))
print(set(rng))
print(tuple(rng))


# map() function

strings = ["Hello World, It is a beautiful day", "Python is awesome", "I am learning Python"]
mapped =map(len, strings)
print((mapped))
print(list(mapped))

mapped = map(lambda x: x.upper(), strings)
print(list(mapped))

mapped = map(lambda x: x.split(), strings)
print(list(mapped))

mapped = map(lambda x: x.split(), strings)
for item in mapped:
    print(item)



# filter() function
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = filter(is_even, numbers)
print(list(filtered))
filtered = filter(lambda x: x > 5, numbers)
print(list(filtered))

# reduce() function
from functools import reduce
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
reduced = reduce(add, numbers)
print(reduced)  # Output: 15

# Using reduce with a lambda function
reduced = reduce(lambda x, y: x + y, numbers)
print(reduced)  # Output: 15

# zip() function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# Unzipping the zipped lists
unzipped = zip(*zip(list1, list2))
print(list(unzipped))  # Output: [(1, 2, 3), ('a', 'b', 'c')]
# Using zip with different lengths
list3 = [4, 5]
zipped = zip(list1, list2, list3)
print(list(zipped))  # Output: [(1, 'a', 4), (2, 'b', 5)]

# enumerate() function
fruits = ['apple', 'banana', 'cherry']
enumerated = enumerate(fruits)
print(list(enumerated))  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# Using enumerate with a start index
enumerated = enumerate(fruits, start=1)
print(list(enumerated))  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# Using enumerate in a loop
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
