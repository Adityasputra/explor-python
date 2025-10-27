"""
Variables in Python
This module demonstrates variable declarations, assignments,
data types, constants, and naming conventions.
"""

# =============================================================================
# BASIC VARIABLE ASSIGNMENTS
# =============================================================================
# Variables are containers for storing data values
# Python is dynamically typed, meaning variable types
# are determined automatically at runtime

print("=== Basic Variable Assignments ===")

name = "adits"        # str
age = 20              # int
is_student = True     # bool
height = 1.95         # float
weight = 80.5         # float
grade = None          # NoneType (absence of value)

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Is student: {is_student} (type: {type(is_student).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Weight: {weight} (type: {type(weight).__name__})")
print(f"Grade: {grade} (type: {type(grade).__name__})\n")


# =============================================================================
# MULTIPLE ASSIGNMENTS
# =============================================================================
# Assign multiple variables in a single line

print("=== Multiple Assignments ===")

x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

a = b = c = 0
print(f"a = {a}, b = {b}, c = {c}")

# Unpacking values from a list
coordinates = [100, 200]
coord_x, coord_y = coordinates
print(f"Coordinates: x = {coord_x}, y = {coord_y}\n")


# =============================================================================
# VARIABLE REASSIGNMENT
# =============================================================================
# Variables can change value and even data type

print("=== Variable Reassignment ===")

value = 42
print(f"Initial value: {value} (type: {type(value).__name__})")

value = "Now I'm a string"
print(f"Reassigned value: {value} (type: {type(value).__name__})")

value = 3.14
print(f"Reassigned again: {value} (type: {type(value).__name__})\n")


# =============================================================================
# VARIABLES IN OPERATIONS
# =============================================================================
# Variables are commonly used in calculations and string operations

print("=== Variables in Operations ===")

# String concatenation
first_name = "aditya"
last_name = "saputra"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Arithmetic operations
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)

print(f"Rectangle - Length: {length}, Width: {width}")
print(f"Area: {area}, Perimeter: {perimeter}")

# Combined calculation example
price = 100
quantity = 3
tax_rate = 0.1

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Shopping - Subtotal: {subtotal}, Tax: {tax}, Total: {total}\n")


# =============================================================================
# CONSTANTS (CONVENTION)
# =============================================================================
# Python does not enforce constants
# Convention: use UPPERCASE variable names

print("=== Constants (Convention) ===")

PI = 3.14159
MAX_USERS = 100
API_KEY = "abc123xyz"
GRAVITY = 9.8

radius = 5
circle_area = PI * radius ** 2
print(f"Circle area with radius {radius}: {circle_area:.2f}\n")


# =============================================================================
# VARIABLE NAMING RULES & BEST PRACTICES
# =============================================================================
# Clear naming improves code readability and maintainability

print("=== Variable Naming Rules ===")

print("RULES:")
print("1. Must start with a letter or underscore (_)")
print("2. Can contain letters, digits, and underscores")
print("3. Case-sensitive (age ≠ Age)")
print("4. Cannot use Python keywords")
print("5. No spaces or special characters\n")

# Valid examples
user_name = "john"
userName = "jane"          # Allowed, but not Pythonic
_private_var = "secret"
number1 = 100
MAX_SIZE = 1000

print("BEST PRACTICES:")
print("- Use descriptive names (user_age > ua)")
print("- Use snake_case for variables and functions")
print("- Use PascalCase for class names")
print("- Use UPPERCASE for constants")
print("- Avoid unclear single-letter names\n")
