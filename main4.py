# unpack elements of an array
colors = ['red', 'blue', 'green']
red, blue, _ = colors

print(red, blue)

# another way to unpack
colors2 = ['red', 'blue', 'green']
# put other elements inside an array
red, *other = colors2

print(f"red: {red}")
print(f"others: {other}")

# iterating over the list

# simple way

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

for index, item in enumerate(cities):
    print(index, item)

# find an index of the element inside array

city_index = cities.index('Cairo')
print(city_index)

# if we don't have such element, it will throw an error

# city_index2 = cities.index('Cairooo')
# print(city_index2)

# in order to use index method, first we need to check is element exists inside an array using in operator

# will get index
if 'Cairo' in cities:
    print(cities.index('Cairo'))

# won't work
if 'Cairooo' in cities:
    print(cities.index('Cairo'))

# iterating using iterator

colors_iter = iter(colors)
color1 = next(colors_iter)
color2 = next(colors_iter)

print(f"color1: {color1}, color2: {color2}")
