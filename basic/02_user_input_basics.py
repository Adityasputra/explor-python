"""
User Input in Python
This module demonstrates how to receive, convert,
validate, and use user input in Python programs.
"""

# =============================================================================
# BASIC USER INPUT
# =============================================================================
# input() is used to receive data from the user
# IMPORTANT: input() ALWAYS returns a string (str)

print("=== Basic User Input ===")

name = input("Enter your name: ")

print(f"Name entered: {name}")
print(f"Type of name variable: {type(name).__name__}\n")


# =============================================================================
# USER INPUT WITH TYPE CONVERSION
# =============================================================================
# To perform calculations, input must be converted
# Common conversions:
# int()   -> whole numbers
# float() -> decimal numbers

print("=== User Input with Type Conversion ===")

age = int(input("Enter your age: "))

print(f"Age entered: {age}")
print(f"Type of age variable: {type(age).__name__}\n")


# =============================================================================
# COMBINING USER INPUT WITH OUTPUT
# =============================================================================
# User input is often used in formatted output (f-string)

print("=== Combining User Input and Output ===")

print(f"Hello, {name}! You are {age} years old.\n")


# =============================================================================
# USER INPUT WITH BASIC VALIDATION
# =============================================================================
# Validation prevents program crashes and incorrect data

print("=== User Input with Validation ===")

user_age = input("Enter your age again: ")

if user_age.isdigit():
    user_age = int(user_age)
    print(f"Valid age entered: {user_age}")
else:
    print("Invalid input! Age must be a number.\n")


# =============================================================================
# MULTIPLE USER INPUTS
# =============================================================================
# Programs often require more than one input

print("=== Multiple User Inputs ===")

city = input("Enter your city: ")
height = float(input("Enter your height (meters): "))

print(f"You live in {city} and your height is {height} meters.\n")
