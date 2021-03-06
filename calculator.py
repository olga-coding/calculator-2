"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator():
    while True:
        things_to_tokenize = input("> ")
        tokens = things_to_tokenize.split(" ")

        if tokens[0] == 'q':
            break
        num1 = float(tokens[1])
        if len(tokens) == 3:
            num2 = float(tokens[2])

        if tokens[0] == "+":
            print(add(num1, num2))
        elif tokens[0] == "-":
            print(subtract(num1, num2))
        elif tokens[0] == "*":
            print(multiply(num1, num2))
        elif tokens[0] == "/":
            print(divide(num1, num2))
        elif tokens[0] == "square":
            print(square(num1))
        elif tokens[0] == "cube":
            print(cube(num1))
        elif tokens[0] == "pow":
            print(pow(num1, num2))
        elif tokens[0] == "mod":
            print(mod(num1, num2))


calculator()
# Your code goes here
