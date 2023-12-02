from functools import partial


def multiply(a, b):
    return a * b


double = partial(multiply, b=2)

result = double(5)
print(result)
