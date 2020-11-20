from art import logo
"""Functions to calculate Addition, Subtraction, Multiplictaion and Division."""

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

"""The calculator function."""
def calculator():
  print (logo)
  num1 = float(input("What is the first number? "))
  for sym in operations:
     print(sym)
    
  is_continue = True
  while is_continue:
    symbol = input("Select an operation: ")
    num2 = float(input("What is the next number? "))
    if symbol not in operations:
      print("Invalid operation selected, start again")
      calculator()
    else:
      selected_symbol = operations[symbol]
      result = selected_symbol(num1, num2)
      print(f"{num1} {symbol} {num2} = {result}")
      new_calc = input(f'Type "Yes" to further your calcalution with {result}, else type "No" to exit\n').lower()

      if new_calc == "yes":
        num1 = result
      elif new_calc == "no":
        is_continue = False
      else:
        print("Invalid input, start again")
        calculator()

calculator()

  
