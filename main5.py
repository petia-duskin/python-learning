from functools import reduce

# map function

numbers = [1, 2, 3, 4, 5]

# map returns an iterator
new_numbers = map(lambda n: n ** 2, numbers)

print(next(new_numbers))
print(next(new_numbers))
print(next(new_numbers))

# transform iterator to a list

colors = ['jane', 'mary', 'lucy']
new_names = map(lambda s: s.capitalize(), colors)

print(list(new_names))

# example of using map

carts = [
    ['SmartPhone', 400],
    ['Tablet', 450],
    ['Laptop', 700]
]

TAX = 0.1

carts = list(map(lambda item: [item[0], item[1], item[1] * TAX], carts))
print(carts)

# filter function

scores = [70, 60, 80, 90, 50]

filtered = filter(lambda score: score >= 70, scores)

print(list(filtered))

# reduce function

scores2 = [70, 65, 100, 110, 5]

sum_result = reduce(lambda prev, current: prev + current, scores2)

print(sum_result)

# list comprehension

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] > 8600]

print(highest_mountains)
