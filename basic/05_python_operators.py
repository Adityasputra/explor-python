"""
Python Operators
This module demonstrates various operators used in Python,
including arithmetic, comparison, logical, assignment,
string, membership, and identity operators.
"""

# =============================================================================
# ARITHMETIC OPERATORS
# =============================================================================
# Arithmetic operators are used to perform mathematical calculations

print("=== Arithmetic Operators ===")

a = 10
b = 15

addition = a + b
subtraction = b - a
multiplication = a * b
division = b / a          # Always returns float
modulus = b % a
floor_division = b // a   # Removes decimal part
exponent = a ** 2

print(f"Addition ({a} + {b}): {addition}")
print(f"Subtraction ({b} - {a}): {subtraction}")
print(f"Multiplication ({a} * {b}): {multiplication}")
print(f"Division ({b} / {a}): {division}")
print(f"Modulus ({b} % {a}): {modulus}")
print(f"Floor Division ({b} // {a}): {floor_division}")
print(f"Exponent ({a} ** 2): {exponent}\n")


# =============================================================================
# COMPARISON OPERATORS
# =============================================================================
# Comparison operators compare values
# Result is always boolean (True / False)

print("=== Comparison Operators ===")

x = 5
y = 10

print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}\n")


# =============================================================================
# LOGICAL OPERATORS
# =============================================================================
# Logical operators combine boolean expressions

print("=== Logical Operators ===")

p = True
q = False

print(f"p and q: {p and q}")   # True if both True
print(f"p or q: {p or q}")     # True if at least one True
print(f"not p: {not p}\n")     # Inverts value


# =============================================================================
# ASSIGNMENT OPERATORS
# =============================================================================
# Used to update variable values efficiently

print("=== Assignment Operators ===")

c = 20
print(f"Initial value of c: {c}")

c += 5
print(f"After c += 5: {c}")

c -= 3
print(f"After c -= 3: {c}")

c *= 2
print(f"After c *= 2: {c}")

c /= 4
print(f"After c /= 4: {c}")

c %= 3
print(f"After c %= 3: {c}\n")


# =============================================================================
# STRING OPERATORS
# =============================================================================
# Operators that work with string data

print("=== String Operators ===")

str1 = "Hello"
str2 = "World"

concatenation = str1 + " " + str2
repetition = str1 * 3

print(f"String concatenation: {concatenation}")
print(f"String repetition: {repetition}\n")


# =============================================================================
# MEMBERSHIP OPERATORS
# =============================================================================
# Used to check if a value exists in a sequence

print("=== Membership Operators ===")

numbers = [1, 2, 3, 4, 5]

print(f"3 in numbers: {3 in numbers}")
print(f"6 not in numbers: {6 not in numbers}\n")


# =============================================================================
# IDENTITY OPERATORS
# =============================================================================
# Used to compare memory location (object identity)

print("=== Identity Operators ===")

a = [1, 2, 3]
b = a              # Same object
c = [1, 2, 3]      # Different object, same value

print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a is not c: {a is not c}")
