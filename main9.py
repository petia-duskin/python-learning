tags = {'django', 'pandas', 'numpy'}

# convert these tags to uppercase

upper_tags = set(map(lambda e: e.upper(), tags))
print(upper_tags)
upper_tags2 = set({e.upper() for e in tags})
print(upper_tags2)

# set operations

s1 = {'java', 'javascript'}
s2 = {'java', 'python'}
s3 = s1.union(s2)

print(s3)

# also we can use | to union sets, but it takes only sets
print(s1 | s2)

# intersection of two sets
intersected_set = s1.intersection(s2)
print(intersected_set)

# or we can use &
intersected_set2 = s1 & s2
print(intersected_set2)

# set difference
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {2, 3, 5, 11, 15, 3, 3, 4}

print(set1.difference(set2))

# another way of difference set
print(set1 - set2)

# symmetric difference
print(set1.symmetric_difference(set2))

# another wat of symmetric difference
print(set1 ^ set2)

# check if a set is a subset of another

set3 = {1, 2, 3, 4}
set4 = {1, 2, 3, 4, 5, 6, 7}

print(set3.issubset(set4))

# check if set is a superset of another

print(set4.issuperset(set3))

# check if sets has no common values

print(s1.isdisjoint(s2))

word1 = "Hello"
word2 = "Wrd"

print(set(word1).isdisjoint(word2))
