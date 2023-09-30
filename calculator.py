#logo
from art import logo
def add(n1, n2):
  return n1 + n2

#substract
def subtract(n1, n2):
  return n1 - n2

#Division
def divide(n1, n2):
  return n1 / n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

operations = {
  "+":add, 
 "-":subtract, 
 "/":divide, 
 "*":multiply
}

def calculator():
  print(logo)
  num1 = float(input("What's is the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True


  while should_continue:
    opertion_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[opertion_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {opertion_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
  