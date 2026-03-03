def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

try:
    n = int(input("How many Fibonacci numbers do you want? "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()
if n <= 0:
    print("Please enter a positive number.")
else:
    result = fibonacci(n)
    print(f"Fibonacci sequence: {result}")
