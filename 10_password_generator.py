import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print("Password Generator")
try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, use_upper, use_digits, use_symbols)
print(f"Generated password: {password}")
