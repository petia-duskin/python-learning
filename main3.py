# tuple - мы не можем менять значения, но может присваивать новую ссылку на tuple
colors = ('red', 'green', 'blue')
print(colors)

colors = ('pink', 'yellow', 'brown', 'cyan', 'magenta')

print(colors)

# sort with strings

guests = ['James', 'Marry', 'Robert', "Jones", 'Alice']
guests.sort(reverse=True)

print(guests)

# sort with numbers

scores = [5, 7, 3, 6, 10, 11]
scores.sort()

print(scores)

# sort with custom compare function

companies = [
    ('Google', 2019, 134.81),
    ('Apple', 2019, 260.2),
    ('Facebook', 2019, 70.7)
]

# sort companies by price
companies.sort(key=lambda c: c[2])

print(companies)

# sort changes the original list, in order to return a new sorted list, you need to use sorted method

numbers2 = [4, 1, 6, 6, 10, 11, 5]

new_numbers2 = sorted(numbers2, reverse=True)

print(new_numbers2)

# we also can pass the same arguments

new_companies = sorted(companies, reverse=False, key=lambda c: c[2])

print(new_companies)

# slicing a list

numbers3 = [i for i in range(10)]

print(numbers3[0:5])

# returns last three elements

print(numbers3[-3:])

# returns every second element of the list

print(numbers3[::2])

# back iteration

print(numbers3[::-1])

# we can substitute parts of the list

colors2 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

colors2[:2] = ['updated_red', 'updated_orange']

print(colors2)

# delete parts of the list

del colors2[0:5]

print(colors2)
