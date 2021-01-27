"""This is a basic calculator."""

# Imports
import os

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


# clear function
def clear():
    """This functions clears the console"""
    return os.system('clear')


# Calculation recursion
def calculator():
    # Default displays
    print(logo)
    print('Operations Symbol:\nAddition is +\nSubtraction is -\nMultiplication is *\nDivision is /\n')

    # The calculator process
    num1 = float(input("What is the first number? "))

    continue_calc = True
    while continue_calc:
        calc_operation = input("What operation do you want to perform? ")
        num2 = float(input("What is the next number? "))

        if calc_operation not in operations:
            clear()
            print("\nInvalid calculation operation, start again.")
            calculator()
        else:
            chosen_operation = operations[calc_operation]
            result = chosen_operation(num1, num2)
            print(f"\n{num1} {calc_operation} {num2} = {result}")
            new_calc = input(f'Type "Yes" to further your calculation with {result}, else type "No" to exit\n').lower()

            if new_calc == "yes":
                num1 = result
            elif new_calc == "no":
                continue_calc = False
                print(f"\nFinal calculation result is: {result}")
            else:
                clear()
                print("Invalid response, start again.")
                calculator()


calculator()
