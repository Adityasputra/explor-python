"""
String Manipulation in Python
This module demonstrates various string operations, manipulation techniques,
and common real-world use cases.
"""

# =============================================================================
# TYPE CONVERSION FUNCTIONS
# =============================================================================
# Convert between different data types: int(), float(), str(), bool()
# IMPORTANT:
# - input() always returns a string
# - Conversion is required for mathematical operations

print("=== Type Conversion ===")

age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1} years old.\n")


# =============================================================================
# STRING LENGTH
# =============================================================================
# len() - Returns the number of characters in a string
# Includes spaces and special characters

print("=== String Length ===")

name = input("Enter your name: ")
print(f"Your name has {len(name)} characters.\n")


# =============================================================================
# INDEXING AND SLICING
# =============================================================================
# Indexing: Access individual characters using [index] (0-based)
# Slicing: Extract substrings using [start:end] (end is exclusive)

print("=== Indexing and Slicing ===")

sample_string = "Hello, World!"

first_character = sample_string[0]      # 'H'
last_character = sample_string[-1]      # '!'
substring = sample_string[7:12]         # 'World'
from_start = sample_string[:5]          # 'Hello'
to_end = sample_string[7:]              # 'World!'

print(f"Original: {sample_string}")
print(f"First character: {first_character}")
print(f"Last character: {last_character}")
print(f"Substring [7:12]: {substring}")
print(f"From start [:5]: {from_start}")
print(f"To end [7:]: {to_end}\n")


# =============================================================================
# STRING METHODS (CASE MANIPULATION)
# =============================================================================
# upper()      - Convert all characters to uppercase
# lower()      - Convert all characters to lowercase
# title()      - Capitalize the first letter of each word
# capitalize() - Capitalize only the first letter of the string

print("=== Case Manipulation ===")

full_name = "aditya saputra"

print(f"Original: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Title Case: {full_name.title()}")
print(f"Capitalized: {full_name.capitalize()}\n")


# =============================================================================
# STRING METHODS (SEARCH AND REPLACE)
# =============================================================================
# replace(old, new) - Replace occurrences of substring
# count(sub)        - Count occurrences of substring
# find(sub)         - Find index (-1 if not found)
# split(separator)  - Split string into list

print("=== Search and Replace ===")

text = "aditya saputra"

print(f"Original: {text}")
print(f"Replace 'saputra' → 'putra': {text.replace('saputra', 'putra')}")
print(f"Count 'a': {text.count('a')}")
print(f"Find 'saputra': {text.find('saputra')}")
print(f"Find 'xyz': {text.find('xyz')}")
print(f"Split by space: {text.split()}\n")


# =============================================================================
# STRING METHODS (WHITESPACE HANDLING)
# =============================================================================
# strip()  - Remove leading and trailing whitespace
# lstrip() - Remove leading whitespace
# rstrip() - Remove trailing whitespace

print("=== Whitespace Handling ===")

raw_input = "   Hello, World!   "

print(f"Original: '{raw_input}'")
print(f"Stripped: '{raw_input.strip()}'")
print(f"Left stripped: '{raw_input.lstrip()}'")
print(f"Right stripped: '{raw_input.rstrip()}'\n")


# =============================================================================
# ESCAPE CHARACTERS
# =============================================================================
# \n - Newline
# \" - Double quote
# \' - Single quote
# \\ - Backslash
# \t - Tab

print("=== Escape Characters ===")

print("Newline example:")
print("Line one\nLine two")

print("\nQuotes example:")
print("He said, \"Hello!\"")
print('She said, \'Hi!\'')

print("\nBackslash example:")
print("Path: C:\\Users\\adits")

print("\nTab example:")
print("Column1\tColumn2\tColumn3\n")


# =============================================================================
# STRING FORMATTING (INTERPOLATION)
# =============================================================================
# f-strings (Python 3.6+) → Recommended
# .format()              → Older but still valid
# % operator             → Legacy (avoid in new code)

print("=== String Formatting ===")

name = "aditya"
age = 20
height = 175.5

# f-string
print(f"My name is {name} and I am {age} years old.")
print(f"Height: {height:.1f} cm")

# format()
print("My name is {} and I am {} years old.".format(name, age))
print("Name: {0}, Age: {1}, Name again: {0}".format(name, age))

# legacy %
print("My name is %s and I am %d years old." % (name, age))
print("Height: %.2f cm" % height)
