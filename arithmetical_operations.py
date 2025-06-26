num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Addition
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# Substraction
sub_result = num1 - num2
print(f"diff: {num1} - {num2} = {sub_result}")

# Multiplication
mult_result = num1 * num2
print(f"mult: {num1} * {num2} = {mult_result}")

# division
if num2 == 0:
    print("Cannot divide by zero")
else:
    div_result = num1 / num2
print(f"div: {num1} / {num2} = {div_result}")