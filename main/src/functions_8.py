
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