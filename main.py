"""This is a basic calculator."""

# Imports
from art import logo


# Basic calculator functions: Addition, Subtraction, Multiplication and Division
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# Calculator operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Default displays
print(logo)
print('Operations Symbol:\nAddition is +\nSubstraction is -\nMultiplication is *\nDivision is /\n')

# The calculator process
num1 = float(input("What is the first number? "))
calc_operation = input("What operation do you want to perform? ")
num2 = float(input("What is the second number? "))

if calc_operation not in operations:
    print("\nInvalid calculation operation.")
else:
    chosen_operation = operations[calc_operation]
    result = chosen_operation(num1, num2)
    print(f"\n{num1} {calc_operation} {num2} = {result}")