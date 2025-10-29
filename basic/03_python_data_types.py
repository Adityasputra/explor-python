"""
Python Data Types
This module demonstrates basic built-in data types in Python,
their usage, characteristics, and common real-world examples.
"""

# =============================================================================
# INTEGER DATA TYPE (int)
# =============================================================================
# Integers are whole numbers (positive, negative, or zero)
# Common use cases:
# - Counting
# - Indexing
# - Financial calculations (without decimals)

print("=== Integer Data Type (int) ===")

age = 20
birth_year = 2005
portfolio_value = 1_000_000  # Underscore improves readability

print(f"Age: {age} (type: {type(age).__name__})")
print(f"Birth year: {birth_year} (type: {type(birth_year).__name__})")
print(f"Portfolio value: {portfolio_value} (type: {type(portfolio_value).__name__})\n")


# =============================================================================
# FLOAT DATA TYPE (float)
# =============================================================================
# Floats represent decimal (floating-point) numbers
# Common use cases:
# - Measurements
# - Scientific calculations
# - Prices with decimals

print("=== Float Data Type (float) ===")

height = 1.95
weight = 80.5
temperature = -2.5

print(f"Height: {height} (type: {type(height).__name__})")
print(f"Weight: {weight} (type: {type(weight).__name__})")
print(f"Temperature: {temperature} (type: {type(temperature).__name__})\n")


# =============================================================================
# STRING DATA TYPE (str)
# =============================================================================
# Strings are sequences of characters
# Used for text data such as names, messages, addresses, etc.

print("=== String Data Type (str) ===")

name = "adits"
address = "123 Main St, Cityville"
greeting = "Hello, World!"

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Address: {address} (type: {type(address).__name__})")
print(f"Greeting: {greeting} (type: {type(greeting).__name__})")

# Single-quoted string
single_quote_str = 'This is a string with single quotes.'

# Triple-quoted string (multi-line)
multi_line_str = """This is a multi-line string.
It can span multiple lines.
Useful for documentation or long text."""

print("\nSingle-quote string example:")
print(single_quote_str)

print("\nMulti-line string example:")
print(multi_line_str)
print()


# =============================================================================
# BOOLEAN DATA TYPE (bool)
# =============================================================================
# Boolean values represent logical truth
# Only two values: True or False
# Heavily used in conditions and control flow

print("=== Boolean Data Type (bool) ===")

is_student = True
has_license = False
is_logged_in = False

print(f"Is student: {is_student} (type: {type(is_student).__name__})")
print(f"Has license: {has_license} (type: {type(has_license).__name__})")
print(f"Is logged in: {is_logged_in} (type: {type(is_logged_in).__name__})\n")


# =============================================================================
# TYPE CHECKING & TYPE CONVERSION
# =============================================================================
# Python allows checking and converting data types dynamically

print("=== Type Checking & Conversion ===")

score_str = "85"
score_int = int(score_str)

print(f"Original: {score_str} (type: {type(score_str).__name__})")
print(f"Converted: {score_int} (type: {type(score_int).__name__})")
