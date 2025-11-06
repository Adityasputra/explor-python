"""
File Handling in Python
This module demonstrates how to read, write, append,
and handle files safely in Python.
"""

# =============================================================================
# OVERVIEW
# =============================================================================
# File handling allows programs to:
# - Store data permanently
# - Read saved data
# - Process large data efficiently
#
# Always use exception handling and the 'with' statement
# to avoid file corruption and memory leaks.
# =============================================================================


# =============================================================================
# FILE MODES
# =============================================================================
# r   -> read (file must exist)
# w   -> write (creates or overwrites file)
# a   -> append (adds content to the end)
# r+  -> read and write
# x   -> create (fails if file already exists)

print("=== File Modes Overview ===")
print("r  - read")
print("w  - write (overwrite)")
print("a  - append")
print("r+ - read & write")
print("x  - create new file\n")


# =============================================================================
# WRITING TO A FILE
# =============================================================================
# Writing data to a file using the with statement

print("=== Writing to a File ===")

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

print("Data written to example.txt\n")


# =============================================================================
# READING FROM A FILE
# =============================================================================
# Reading entire file content

print("=== Reading from a File ===")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)


# =============================================================================
# APPENDING TO A FILE
# =============================================================================
# Adding new content without removing existing data

print("=== Appending to a File ===")

with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

print("New content appended.\n")


# =============================================================================
# READING UPDATED FILE CONTENT
# =============================================================================

print("=== Updated File Content ===")

with open("example.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)


# =============================================================================
# REAL USE CASE: SAVING STUDENT SCORES
# =============================================================================
# Simulates saving student data in a school system

print("=== Saving Student Scores ===")

with open("student_scores.txt", "w") as file:
    while True:
        try:
            name = input("Enter student name (or 'exit' to finish): ").strip()

            if name.lower() == "exit":
                break

            if not name:
                raise ValueError("Name cannot be empty")

            score = int(input(f"Enter score for {name}: "))

            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")

            file.write(f"{name}: {score}\n")

        except ValueError as error:
            print("Input error:", error)

print("Student scores saved successfully.\n")


# =============================================================================
# READING STUDENT SCORES
# =============================================================================
# Reading file line by line (memory efficient)

print("=== Reading Student Scores ===")

try:
    with open("student_scores.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Score file not found.")

print()


# =============================================================================
# FILE ERROR HANDLING
# =============================================================================
# Handling missing files safely

print("=== File Error Handling ===")

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("File operation finished.\n")


# =============================================================================
# BEST PRACTICES
# =============================================================================
print("=== Best Practices ===")
print("- Always use 'with open()' instead of open() alone")
print("- Handle FileNotFoundError for safer programs")
print("- Validate user input before saving to files")
print("- Use append mode ('a') when you don't want to lose data")
print("- Close files properly (handled automatically by 'with')")
