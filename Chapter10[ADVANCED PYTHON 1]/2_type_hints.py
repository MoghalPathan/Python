#Type hints (basic and advanced): you write what type of data a variable or function should use.


def add(a: int, b: int) -> int:
    return a + b
#a: int means a should be an integer.
#-> int means the function returns an integer.

#Important: Python does NOT enforce this.




print(add("Hi ", "there"))   # still works and prints: Hi there
"""
So why use them?

Your editor (VS Code) shows warnings when you pass the wrong type.
Code is easier to read. You instantly know what a function expects.
Tools like mypy can check your whole project for type mistakes.
"""



#Advanced type hints:
from typing import Optional, Union, Callable

# List of something
def total(prices: list[float]) -> float:
    return sum(prices)

# Dictionary: keys are str, values are int
def marks() -> dict[str, int]:
    return {"maths": 90, "python": 95}

# Tuple with fixed types
def point() -> tuple[int, int]:
    return (3, 4)

# Value can be int OR None (very common)
def greet(name: str, age: int | None = None) -> str:
    if age is None:
        return f"Hello {name}"
    return f"Hello {name}, age {age}"

# Older way to write the same: Optional[int]  ==  int | None
def find_user(uid: int) -> Optional[str]:
    users = {1: "Naved", 2: "Mansi"}
    return users.get(uid)      # returns None if not found

# Either int or str
def show(value: Union[int, str]) -> None:   # same as int | str
    print(value)

# A function passed as a parameter
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(lambda x, y: x * y, 4, 5))   # 20

#How to read Callable[[int, int], int]: a function that takes two ints and returns an int.





#Variable hints:
age: int = 22
names: list[str] = ["a", "b"]

#None as a return type means the function returns nothing.

