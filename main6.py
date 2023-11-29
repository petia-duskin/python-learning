# dictionaries

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# first way tp get value, will throw an error if key doesn't exist

print(person['first_name'])

# second way to get value, not throw an error if key doesn't exist

print(person.get('first_name'))

# return default value is key doesn't exist

print(person.get('age1', 18))

# change value

person['age'] = 55

print(person['age'])

# remove key-value pairs

del person['age']

print(person)

# examine a dictionary

for key, value in person.items():
    print(f"key: {key}, value: {value}")


# loop over the keys

for key in person.keys():
    print(f"key: {key}")


# loop over the values

for value in person.values():
    print(value)


