from typing import List, Tuple, Dict, Optional, Union, Callable


# =========================
# A. Simple function
# =========================

# This function adds two integers and returns the result
def add(a: int, b: int) -> int:
    return a + b


# =========================
# B. Work with list
# =========================

# This function returns the sum of all elements in a list
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


# =========================
# C. Tuple example
# =========================

# This function returns a tuple with number and its square
def number_and_square(x: int) -> Tuple[int, int]:
    return x, x * x


# =========================
# D. Dictionary example
# =========================

# This function returns the value by key or None if key not found
def get_value(data: Dict[str, int], key: str) -> Optional[int]:
    return data.get(key)


# =========================
# E. Union example
# =========================

# This function accepts int or float and returns it as float
def to_float(value: Union[int, float]) -> float:
    return float(value)


# =========================
# F. Higher-order function
# =========================

# This function applies another function to a number
def apply_function(x: int, func: Callable[[int], int]) -> int:
    return func(x)


# =========================
# G. Lambda example
# =========================

# Lambda function to double a number
double = lambda x: x * 2


# =========================
# Demonstration
# =========================

if __name__ == "__main__":
    print("Task A:", add(2, 3))

    print("Task B:", sum_list([1, 2, 3, 4]))

    print("Task C:", number_and_square(5))

    print("Task D:", get_value({"a": 10, "b": 20}, "a"))

    print("Task E:", to_float(7))

    print("Task F:", apply_function(5, double))

    print("Task G:", double(10))
