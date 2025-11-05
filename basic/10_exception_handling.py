"""
Exception Handling in Python
This module demonstrates how to handle runtime errors
using try, except, else, and finally blocks.
"""

# =============================================================================
# OVERVIEW
# =============================================================================
# Exception handling is used to:
# - Prevent program crashes
# - Handle unexpected runtime errors
# - Provide user-friendly error messages
#
# Common built-in exceptions:
# - ValueError
# - ZeroDivisionError
# - TypeError
# - FileNotFoundError
# =============================================================================


# =============================================================================
# BASIC TRY - EXCEPT - ELSE - FINALLY
# =============================================================================
print("=== Basic Try - Except - Else - Finally ===")

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    # Raised when input cannot be converted to an integer
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    # Raised when dividing by zero
    print("Error: Division by zero is not allowed.")

else:
    # Executed if no exception occurs
    print(f"Result: {result}")

finally:
    # Always executed (cleanup, closing resources, etc.)
    print("Execution completed.\n")


# =============================================================================
# MULTIPLE EXCEPTIONS IN ONE BLOCK
# =============================================================================
print("=== Multiple Exceptions in One Block ===")

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero occurred.")

print()


# =============================================================================
# CATCHING ALL EXCEPTIONS (NOT RECOMMENDED)
# =============================================================================
# Use this carefully, mainly for debugging
print("=== Catching All Exceptions ===")

try:
    data = int("abc")  # This will raise ValueError
except Exception as e:
    print("An error occurred:", e)

print()


# =============================================================================
# REAL USE CASE: USER LOGIN ATTEMPT
# =============================================================================
print("=== Use Case: Login System ===")

correct_password = "admin123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        password = input("Enter your password: ")

        if not password:
            raise ValueError("Password cannot be empty")

        if password == correct_password:
            print("Login successful. Welcome!")
            break
        else:
            print("Incorrect password.")

    except ValueError as error:
        print("Error:", error)

    finally:
        attempts += 1
        print(f"Attempt {attempts}/{max_attempts}\n")

else:
    print("Too many failed attempts. Access denied.")

print()


# =============================================================================
# REAL USE CASE: AGE VALIDATION
# =============================================================================
print("=== Use Case: Age Validation ===")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print(f"Your age is valid: {age}")

except ValueError as e:
    print("Invalid age:", e)

print()


# =============================================================================
# CUSTOM ERROR MESSAGE WITH raise
# =============================================================================
print("=== Raising Custom Errors ===")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    remaining_balance = withdraw(500, 700)
    print(f"Remaining balance: {remaining_balance}")
except ValueError as error:
    print("Transaction failed:", error)

print()


# =============================================================================
# BEST PRACTICES
# =============================================================================
print("=== Best Practices ===")
print("- Catch specific exceptions instead of using bare except")
print("- Use else for code that should run only if no error occurs")
print("- Use finally for cleanup actions (closing files, releasing resources)")
print("- Avoid silent failures (always log or show error messages)")
print("- Use raise to enforce validation rules")
