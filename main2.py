# how to create comments of a function
def some_func(name, age):
    "Return your name and age"
    print(f"Your name is {name} and your age is {age}")


some_func(name="John", age=15)
some_func("John", 15)


def add(a, b):
    "Return the sum of two arguments"
    return a + b


# how to print info about function
help(add)
