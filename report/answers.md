# Answers

Question 1: What is the purpose of type hints in Python?

Answer:
Type hints are used to describe the expected types of variables and function arguments.
They help developers understand the code better and allow tools like mypy to detect errors before running the program.
This is useful for improving code reliability and readability.

---

Question 2: What is the difference between Any and a generic type T?

Answer:
Any means that a variable can have any type and no type checking is performed.
A generic type T represents a specific but unknown type that remains consistent.
This is useful for writing flexible but still type-safe code.

---

Question 3: What does Callable[[int], int] describe?

Answer:
Callable[[int], int] describes a function that takes an integer as input and returns an integer.
This is useful when passing functions as arguments and ensuring they match the expected signature.

---

Question 4: Why does mypy --strict require more annotations?

Answer:
The strict mode requires more explicit type information to ensure higher code safety.
It reduces ambiguity and helps catch more potential errors.
This is useful for writing more reliable and maintainable code.
