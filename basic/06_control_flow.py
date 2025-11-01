"""
Control Flow in Python
This module demonstrates conditional statements, logical operators,
and decision-making structures in Python.
"""

# =============================================================================
# BASIC IF STATEMENT
# =============================================================================
# The if statement executes code when a condition evaluates to True

print("=== Basic if Statement ===")

number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative.")

if number > 0:
    print("The number is positive.")

if number == 0:
    print("The number is zero.")

print()


# =============================================================================
# IF - ELIF - ELSE STATEMENT
# =============================================================================
# Used to check multiple conditions in sequence
# Only ONE block will be executed

print("=== If - Elif - Else Statement ===")

score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent work!")
elif score >= 75:
    print("Good job!")
elif score >= 60:
    print("You passed.")
else:
    print("Keep trying to improve your score!")

print()


# =============================================================================
# LOGICAL OPERATORS (and, or, not)
# =============================================================================
# Combine multiple conditions into a single decision

print("=== Logical Operators ===")

age = int(input("Enter your age: "))
drive_license = input("Do you have a Drive License? (yes/no): ").lower()

if drive_license not in ("yes", "no"):
    print("Invalid input for Drive License status.")
elif age >= 18 and drive_license == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

print()


# =============================================================================
# NESTED IF STATEMENT
# =============================================================================
# An if statement inside another if statement
# Useful for hierarchical or dependent conditions

print("=== Nested if Statement ===")

temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 30:
    if temperature > 40:
        print("It's extremely hot!")
    else:
        print("It's a hot day.")
elif temperature < 15:
    if temperature < 0:
        print("It's freezing cold!")
    else:
        print("It's a cold day.")
else:
    print("The weather is moderate.")

print()


# =============================================================================
# USER AUTHENTICATION (NESTED IF EXAMPLE)
# =============================================================================
# Simple username and password validation logic

print("=== Simple Authentication Example ===")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "admin123":
        print("Access granted. Welcome, admin!")
    else:
        print("Incorrect password for admin.")
else:
    print("Unknown username.")

print()


# =============================================================================
# MATCH - CASE STATEMENT (Python 3.10+)
# =============================================================================
# Used as a cleaner alternative to multiple elif statements

print("=== Match - Case Statement ===")

day = input("Enter a day of the week: ").lower()

match day:
    case "monday":
        print("Start of the work week.")
    case "wednesday":
        print("Midweek day.")
    case "friday":
        print("End of the work week.")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("Just another day.")

print()


# =============================================================================
# TERNARY (CONDITIONAL) EXPRESSION
# =============================================================================
# A compact way to write a simple if-else statement

print("=== Ternary Operator ===")

age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"
print(f"You are classified as: {status}")
