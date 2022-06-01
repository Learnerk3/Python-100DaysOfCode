import calcLogo
import os
# def math_operation(operation, firstNumber, secondNumber):
#     if operation == "+":
#         return firstNumber + secondNumber
#     elif operation == "-":
#         return firstNumber - secondNumber
#     elif operation == "*":
#         return firstNumber * secondNumber
#     else:
#         return firstNumber/secondNumber

  
# operation_list = ["+", "-", "*", "/"]
# is_calculating = True
# while is_calculating:
#     print(calcLogo.logo)
#     first_number = float(input("What's your first number?: "))
#     for operation in operation_list:
#         print(operation)
#     operation_choice = input("Pick an operation: ")
#     second_number = float(input("What's your next number?: "))
#     result = math_operation(operation_choice, first_number, second_number)
#     print(f"{first_number} {operation_choice} {second_number} = {result}")

#     user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#     while user_choice == 'y':
#         first_number = result
#         operation_choice = input("Pick an operation: ")
#         second_number = float(input("What's your next number?: "))
#         result = math_operation(operation_choice, first_number, second_number)
#         print(f"{first_number} {operation_choice} {second_number} = {result}")
#         user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#     os.system("cls")
#     print(calcLogo.logo)

#Add
def add(num1, num2):
    return num1 + num2

#Subtract
def subtract(num1, num2):
    return num1 - num2

#Multiply
def multiply(num1, num2):
    return num1 * num2

#Divition
def divition(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divition
}
def calculator():
    print(calcLogo.logo)
    num1 = float(input("What's your first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's your next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
