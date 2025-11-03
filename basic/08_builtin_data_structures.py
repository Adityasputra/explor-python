"""
Python Built-in Data Structures
This module demonstrates List, Tuple, Dictionary, and Set in Python,
including explanations, best practices, and simple real-world use cases.
"""

# =============================================================================
# OVERVIEW
# =============================================================================
# Python provides several built-in data structures to store collections of data.
# Choosing the right data structure improves code readability and performance.
#
# Main data structures:
# - List       : Ordered, mutable, allows duplicates
# - Tuple      : Ordered, immutable, allows duplicates
# - Dictionary : Key-value pairs, mutable, keys must be unique
# - Set        : Unordered, mutable, does NOT allow duplicates
# =============================================================================


# =============================================================================
# LIST
# =============================================================================
# Lists are ordered, mutable (can be changed), and allow duplicate values.
# Best used when data changes frequently.

print("=== List ===")

data = []
print(f"Type of data: {type(data).__name__}")

# List with mixed data types
mixed_data = [1, "two", 3.0, True]
print(f"Mixed data list: {mixed_data}")

# Accessing elements
print(f"Second element: {mixed_data[1]}")
print(f"Last element: {mixed_data[-1]}")

# Modifying elements
mixed_data[0] = 10
print(f"After modification: {mixed_data}")

# Adding elements
mixed_data.append("new item")
mixed_data.insert(2, "inserted item")
print(f"After adding items: {mixed_data}")

# Removing elements
mixed_data.remove("two")
mixed_data.pop()
del mixed_data[1]
print(f"After removing items: {mixed_data}")

print(f"Length of list: {len(mixed_data)}")

# Iteration
print("\nIterating over list:")
for item in mixed_data:
    print(item)

# Membership test
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")

print()


# =============================================================================
# LIST USE CASE: SHOPPING CART
# =============================================================================
print("=== List Use Case: Shopping Cart ===")

cart = []
cart.append("Apple")
cart.append("Milk")
cart.append("Bread")

cart.remove("Milk")

print("Shopping Cart Items:")
for item in cart:
    print("-", item)

print()


# =============================================================================
# TUPLE
# =============================================================================
# Tuples are ordered and immutable.
# Best used for fixed data that should not change.

print("=== Tuple ===")

data_tuple = (1, "two", 3.0, True)
print(f"Type: {type(data_tuple).__name__}")
print(f"Content: {data_tuple}")

print("\nIterating over tuple:")
for item in data_tuple:
    print(item)

# Common tuple usage
RGB_WHITE = (255, 255, 255)
SCREEN_SIZE = (1920, 1080)

print(f"\nRGB White: {RGB_WHITE}")
print(f"Screen size: {SCREEN_SIZE}")

print()


# =============================================================================
# TUPLE USE CASE: LOCATION COORDINATES
# =============================================================================
print("=== Tuple Use Case: Coordinates ===")

location = (106.8456, -6.2088)  # longitude, latitude
print(f"Location coordinates: {location}")

print()


# =============================================================================
# DICTIONARY
# =============================================================================
# Dictionaries store data in key-value pairs.
# Best used for structured data.

print("=== Dictionary ===")

user = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}

print(f"Type: {type(user).__name__}")
print(f"User data: {user}")

# Access and modify
print(f"User name: {user['name']}")
user["age"] = 31

# Add new data
user["city"] = "New York"

# Safe access
email = user.get("email", "Not provided")

print(f"Updated user: {user}")
print(f"Email: {email}")

print("\nIterating dictionary:")
for key, value in user.items():
    print(f"{key}: {value}")

print()


# =============================================================================
# DICTIONARY USE CASE: USER LOGIN DATA
# =============================================================================
print("=== Dictionary Use Case: User Profile ===")

profile = {
    "username": "adits",
    "email": "adits@mail.com",
    "is_active": True
}

if profile["is_active"]:
    print(f"Welcome, {profile['username']}!")

print()


# =============================================================================
# SET
# =============================================================================
# Sets are unordered and do not allow duplicate values.
# Best used for membership testing and removing duplicates.

print("=== Set ===")

numbers = {1, 2, 3, 4, 5}
print(f"Type: {type(numbers).__name__}")
print(f"Initial set: {numbers}")

numbers.add(6)
numbers.remove(3)
print(f"After modifications: {numbers}")

print(f"Is 4 in set? {4 in numbers}")
print(f"Is 10 in set? {10 in numbers}")

print("\nIterating over set:")
for num in numbers:
    print(num)

print()


# =============================================================================
# SET USE CASE: EMAIL DUPLICATION CHECK
# =============================================================================
print("=== Set Use Case: Email Validation ===")

registered_emails = {"a@mail.com", "b@mail.com"}

new_email = "a@mail.com"

if new_email in registered_emails:
    print("Email already registered.")
else:
    registered_emails.add(new_email)
    print("Email successfully registered.")

print()


# =============================================================================
# SUMMARY
# =============================================================================
print("=== Summary ===")
print("- List       : Ordered, mutable, allows duplicates")
print("- Tuple      : Ordered, immutable")
print("- Dictionary : Key-value pairs, fast access")
print("- Set        : Unique items, fast membership testing")
