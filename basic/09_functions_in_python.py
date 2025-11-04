"""
Functions in Python
This module demonstrates function definitions, parameters,
return values, scope, and advanced function concepts with simple use cases.
"""

# =============================================================================
# OVERVIEW
# =============================================================================
# A function is a reusable block of code that performs a specific task.
# Functions help:
# - Avoid code repetition
# - Improve readability
# - Make programs easier to maintain
# =============================================================================


# =============================================================================
# BASIC FUNCTION DEFINITION AND CALL
# =============================================================================
print("=== Basic Function ===")

def say_hello():
    """Prints a simple greeting message."""
    print("Hello!")

say_hello()
print()


# =============================================================================
# FUNCTION WITH PARAMETERS
# =============================================================================
print("=== Function with Parameters ===")

def say_goodbye(name):
    """Prints a goodbye message using a name parameter."""
    print(f"Goodbye, {name}!")

say_goodbye("Alice")
print()


# =============================================================================
# FUNCTION WITH RETURN VALUE
# =============================================================================
print("=== Function with Return Value ===")

def rectangle_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

area = rectangle_area(5, 3)
print(f"Area of rectangle: {area}")

def circle_area(radius):
    """Returns the area of a circle."""
    PI = 3.14159
    return PI * radius ** 2

area1 = circle_area(4)
area2 = circle_area(7)

print(f"Area of circle (r=4): {area1:.2f}")
print(f"Area of circle (r=7): {area2:.2f}")
print(f"Total area: {area1 + area2:.2f}")
print()


# =============================================================================
# FUNCTION USE CASE: ROOM CALCULATION
# =============================================================================
print("=== Use Case: Room Area Calculator ===")

def room_area(length, width):
    return length * width

room1 = room_area(4, 5)
room2 = room_area(3, 6)

print(f"Room 1 area: {room1} m²")
print(f"Room 2 area: {room2} m²")
print()


# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================
print("=== Default Parameters ===")

def greet(name="Guest"):
    """Greets user, defaults to 'Guest'."""
    print(f"Welcome, {name}!")

greet()
greet("Bob")
print()


# =============================================================================
# KEYWORD ARGUMENTS
# =============================================================================
print("=== Keyword Arguments ===")

def introduce(first_name, last_name):
    print(f"My name is {first_name} {last_name}.")

introduce(last_name="Smith", first_name="John")
print()


# =============================================================================
# RECURSIVE FUNCTION
# =============================================================================
print("=== Recursive Function ===")

def factorial(n):
    """
    Calculates factorial using recursion.
    WARNING: Avoid large n to prevent stack overflow.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print()


# =============================================================================
# VARIABLE-LENGTH ARGUMENTS (*args)
# =============================================================================
print("=== Variable-Length Arguments (*args) ===")

def sum_all(*args):
    """Returns the sum of all given numbers."""
    return sum(args)

total = sum_all(1, 2, 3, 4, 5)
print(f"Sum of all numbers: {total}")
print()


# =============================================================================
# *args USE CASE: STUDENT SCORES
# =============================================================================
print("=== Use Case: Student Scores ===")

def average_score(*scores):
    return sum(scores) / len(scores)

avg = average_score(80, 90, 75, 88)
print(f"Average score: {avg:.2f}")
print()


# =============================================================================
# VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# =============================================================================
print("=== Variable-Length Keyword Arguments (**kwargs) ===")

def print_info(**kwargs):
    """Prints key-value information."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=30, city="New York")
print()


# =============================================================================
# **kwargs USE CASE: USER PROFILE
# =============================================================================
print("=== Use Case: User Profile ===")

def create_profile(**data):
    print("User Profile:")
    for key, value in data.items():
        print(f"- {key}: {value}")

create_profile(username="adits", email="adits@mail.com", is_active=True)
print()


# =============================================================================
# LAMBDA FUNCTION
# =============================================================================
print("=== Lambda Function ===")

square = lambda x: x * x
print(f"Square of 6: {square(6)}")
print()


# =============================================================================
# HIGHER-ORDER FUNCTION
# =============================================================================
print("=== Higher-Order Function ===")

def apply_function(func, value):
    """Applies a function to a value."""
    return func(value)

result = apply_function(lambda x: x + 10, 5)
print(f"Result: {result}")
print()


# =============================================================================
# NESTED FUNCTIONS
# =============================================================================
print("=== Nested Functions ===")

def outer_function(message):
    def inner_function():
        print(message)
    inner_function()

outer_function("Hello from the outer function!")
print()


# =============================================================================
# VARIABLE SCOPE (GLOBAL vs LOCAL)
# =============================================================================
print("=== Variable Scope ===")

x = 10  # Global variable

def modify_global():
    global x
    x = 20

modify_global()
print(f"Global x after modification: {x}")
print()


# =============================================================================
# BEST PRACTICES SUMMARY
# =============================================================================
print("=== Best Practices ===")
print("- Use descriptive function names (verb-based)")
print("- Keep functions small and focused")
print("- Use return instead of print when possible")
print("- Avoid global variables unless necessary")
print("- Add docstrings for clarity")
