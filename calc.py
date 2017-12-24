import math

op = input("Operation to be used:")
a = int(input("First number:"))
b = int(input("Second number:"))

def add():
  if op in ["+", "add", "addition"]:
    ans = a + b
    print(ans)

def subtract():
  if op in ["-", "subtract", "subtraction"]:
    ans = a - b
    print(ans)

def divide():
  if op in ["/", "divide", "division"]:
    ans = a / b
    print(ans)

def multiply():
  if op in ["x", "X", "*", "multiply", "multiplication"]:
    ans = a * b
    print(ans)

add()
subtract()
divide()
multiply()