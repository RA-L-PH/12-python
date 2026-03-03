try:
    n = int(input("Enter the upper limit for FizzBuzz: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
