def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    return k - 273.15


def get_temperature() -> float | None:
    """Prompt for and validate temperature input."""
    raw = input("Enter temperature: ").strip()
    if not raw:
        print("Error: Temperature cannot be empty.")
        return None
    try:
        return float(raw)
    except ValueError:
        print("Error: Invalid number. Please enter a numeric value.")
        return None


def get_choice() -> str | None:
    """Prompt for and validate menu choice."""
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose an option (1-4): ").strip()
    if choice not in ("1", "2", "3", "4"):
        print("Error: Invalid choice. Please enter 1-4.")
        return None
    return choice


def convert(choice: str, temp: float) -> str | None:
    """Perform conversion and return result string, or None on error."""
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        if temp < -273.15:
            print("Error: Celsius below absolute zero (-273.15°C).")
            return None
        return f"{temp}°C = {result:.2f}°F"
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        if temp < -459.67:
            print("Error: Fahrenheit below absolute zero (-459.67°F).")
            return None
        return f"{temp}°F = {result:.2f}°C"
    elif choice == "3":
        if temp < -273.15:
            print("Error: Celsius below absolute zero (-273.15°C).")
            return None
        result = celsius_to_kelvin(temp)
        return f"{temp}°C = {result:.2f} K"
    else:
        if temp < 0:
            print("Error: Kelvin cannot be negative.")
            return None
        result = kelvin_to_celsius(temp)
        return f"{temp} K = {result:.2f}°C"


def main() -> None:
    """Run the temperature converter."""
    choice = get_choice()
    if choice is None:
        return
    temp = get_temperature()
    if temp is None:
        return
    result = convert(choice, temp)
    if result:
        print(result)


if __name__ == "__main__":
    main()
