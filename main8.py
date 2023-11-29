# set type

skills = {'Python', 'JavaScript', 'Java'}

# if we need an empty set we use the following construction

empty_set = set()

# create set with iterable
# the original order of elements can be not saved
skills2 = set(['java', 'php', 'python'])

print(skills2)

# set functions removes duplicates
skills3 = {'1', '1', '2', '3', '4', '5'}

print(skills3)
print(len(skills3))

# adding and removing elements of a set

skills.add('new element')
skills.remove('new element')

# discard method remove an element from set and not raise an error

skills.discard('ldep')

# remove element from tail, every time it returns different values

print(skills.pop())
print(skills.pop())

# remove all elements from a set
skills.clear()

# make set immutable

skills = {'first', 'second', 'third'}
skills = frozenset(skills)
# now we can't add or remove elements from skills


# also we can change start index of enumerate
for index, skill in enumerate(skills, 1):
    print(f"index: {index}, skill: {skill}")
