# What's the first number?: 
# + or - or * or /
# Pick an operation
# Next number?

import calculator_art as art

print(art.logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

calc_dict = {
  "+": add,
  "-": subtract,
  "*": mult,
  "/": div,
}

cont = True

calc_result = 0

while cont == True:
  first_number = float(input("What's the first number?: "))
  operator = input("Pick an operation: ")
  second_number = float(input("What's the next number?: "))

  calc_result = calc_dict[operator](first_number, second_number)
  print(f"{first_number} {operator} {second_number} = {calc_result}")

  cont_input = input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation: ")
  if cont_input == 'n':
    cont = False
  else:
    continue
