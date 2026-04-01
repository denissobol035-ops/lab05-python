# LAB05 – Type Hints, Generics, Mypy

from typing import List, Optional, Callable, TypeVar

# -----------------------------
# Task A — Basic Type Hints
# -----------------------------

def add(a: int, b: int) -> int:
    return a + b

def square_list(data: List[int]) -> List[int]:
    return [x * x for x in data]

print("Task A")
print(add(2, 3))
print(square_list([1, 2, 3]))


# -----------------------------
# Task B — Typed Collections
# -----------------------------

def filter_even(data: List[int]) -> List[int]:
    return [x for x in data if x % 2 == 0]

print()
print("Task B")
print(filter_even([1, 2, 3, 4, 5, 6]))


# -----------------------------
# Task C — Optional
# -----------------------------

def find(data: List[int], x: int) -> Optional[int]:
    for item in data:
        if item == x:
            return item
    return None

print()
print("Task C")
print(find([1, 2, 3], 2))   # found
print(find([1, 2, 3], 10))  # not found


# -----------------------------
# Task D — Function Type
# -----------------------------

def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

print()
print("Task D")
print(apply(lambda x: x + 1, 5))
print(apply(lambda x: x * 2, 5))


# -----------------------------
# Task E — Generics
# -----------------------------

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

print()
print("Task E")
print(first([1, 2, 3]))
print(first(["a", "b", "c"]))


# -----------------------------
# Task F — Function Returning Function
# -----------------------------

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiply(x: int) -> int:
        return x * k
    return multiply

print()
print("Task F")
times3 = make_multiplier(3)
print(times3(5))


# -----------------------------
# Task G — Pipeline
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = sum(x * x for x in numbers if x % 2 == 0)


print()
print("Task G")
print(result)
