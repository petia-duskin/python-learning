# swap values of two elements
x = 10
y = 20

x, y = y, x

print(f"x:{x}, y:{y}")

# star is also used to unpack tuple

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

# merge them into single tuple
numbers = (*odd_numbers, *even_numbers)
print(numbers)


# the same concept for the function arguments

def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)
print(result)


# also it is possible to do the following

def add2(x, y, *args, z):
    return x + y + sum(args) + z


print(add2(10, 20, 30, 40, z=50))


# kwargs parameters, it always must be placed in the tail
# dict type parameters

def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)


connect(server="localhost", port=3306, user="root")

# if we want to pass a dict, we need to add **

config = {
    'server': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'deodpeo242ko3ej'
}

connect(**config)


# using both *args and **kwargs arguments
def fn(*args, **kwargs):
    print(args)
    print(kwargs)


fn(1, 2, 3, x=10, y=20, z=30)
