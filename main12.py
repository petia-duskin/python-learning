from typing import Union, List


# type hints

def say_hi(name: str) -> str:
    return f"Hello, {name}"


print(say_hi("Petia"))

number = Union[int, float]


def add(x: number, y: number) -> number:
    return x + y


ratings: List[int] = [1, 2, 3]


def log(message: str) -> None:
    print(message)
