"""
Loops in Python
This module demonstrates for-loops, while-loops,
and loop control statements (break, continue, else).
"""

# =============================================================================
# FOR LOOP WITH range()
# =============================================================================
# Used to repeat actions a specific number of times

print("=== For Loop with range() ===")

# Print indexes from 0 to 4
for i in range(5):
    print(f"Index: {i}")

print()

# Print numbers from 1 to 5
for number in range(1, 6):
    print(f"Number: {number}")

print()

# Repeat a message multiple times
for _ in range(3):
    print("Hello!")

print()

# Reverse loop from 5 to 1
for i in range(5, 0, -1):
    print(f"Reverse index: {i}")

print()


# =============================================================================
# ITERATING OVER A STRING
# =============================================================================
# Strings are iterable (character by character)

print("=== Iterating Over a String ===")

word = "Python"

for char in word:
    print(f"Character: {char}")

print()


# =============================================================================
# WHILE LOOP
# =============================================================================
# Used when the number of iterations is unknown

print("=== While Loop ===")

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # IMPORTANT: prevents infinite loop

print()


# =============================================================================
# WHILE LOOP WITH CONDITION AND LIMIT
# =============================================================================
# Commonly used for authentication or retry systems

print("=== While Loop with Condition and Limit ===")

password = ""
attempt = 1
max_attempts = 3

while password != "secret" and attempt <= max_attempts:
    password = input("Enter your password: ")

    if password == "secret":
        print("Access confirmed.")
    else:
        print("Access denied.")

    attempt += 1

print("Process closed.\n")


# =============================================================================
# BREAK STATEMENT
# =============================================================================
# Immediately stops the loop

print("=== Break Statement Example ===")

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Enter your number (1-10): "))

    if guess == secret_number:
        print("Your number is correct!")
        break
    else:
        print("Wrong guess. Try again.")

print("Game closed.\n")


# =============================================================================
# CONTINUE STATEMENT
# =============================================================================
# Skips the current iteration and continues with the next one

print("=== Continue Statement Example ===")

for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

print()


# =============================================================================
# FOR LOOP WITH ELSE
# =============================================================================
# else executes ONLY if loop ends without break

print("=== For Loop with else ===")

word = input("Enter your word: ")
search_char = input("Enter a character to find: ")

for char in word:
    if char == search_char:
        print(f"Character '{search_char}' was found.")
        break
else:
    print(f"Character '{search_char}' was not found.")

print()


# =============================================================================
# WHILE LOOP WITH ELSE
# =============================================================================
# else runs when the loop condition becomes False naturally

print("=== While Loop with else ===")

correct_password = "admin123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Access successful. Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        print(f"Incorrect password. Attempts left: {remaining}")
else:
    print("Too many failed attempts. Access denied.")

print()


# =============================================================================
# NESTED LOOPS
# =============================================================================
# Used for grids, tables, matrices, and combinations

print("=== Multiplication Table ===")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()
