def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
print("Operations: +, -, *, /")

try:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

if op == "+":
    print(f"Result: {add(a, b)}")
elif op == "-":
    print(f"Result: {subtract(a, b)}")
elif op == "*":
    print(f"Result: {multiply(a, b)}")
elif op == "/":
    print(f"Result: {divide(a, b)}")
else:
    print("Invalid operator")
