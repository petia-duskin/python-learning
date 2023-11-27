import keyword

# print all keywords
print(keyword.kwlist)

age = int(input("tell us your age: "))

# ternary expression
ticket_price = 20 if age >= 18 else 5

# start, end, step
for i in range(0, 11, 2):
    print(i)

# we take only what typed, without '>'
command = input('>')
print(command)
