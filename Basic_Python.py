# Variables and Data Types
x, y = 5, 3.2
name = "Alice"

# Lists, Loops, and Conditions
nums = [1, 2, 3, 4]
for n in nums:
    print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")

# Functions and Lambdas
square = lambda n: n * n
print("Square of 5:", square(x))

# Classes and Objects
class Greeter:
    def __init__(self, name): self.name = name
    def greet(self): return f"Hello, {self.name}!"

print(Greeter(name).greet())

# File I/O
with open("test.txt", "w") as f: f.write("Hello, file!")
with open("test.txt") as f: print(f.read())

# Exceptions
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# List Comprehensions
squares = [n**2 for n in nums]
print("Squares:", squares)
