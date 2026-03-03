def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")

choice = input("Choose an option (1-4): ")
try:
    value = float(input("Enter value: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

if choice == "1":
    print(f"{value} km = {km_to_miles(value):.4f} miles")
elif choice == "2":
    print(f"{value} miles = {miles_to_km(value):.4f} km")
elif choice == "3":
    print(f"{value} kg = {kg_to_pounds(value):.4f} pounds")
elif choice == "4":
    print(f"{value} pounds = {pounds_to_kg(value):.4f} kg")
else:
    print("Invalid choice")
