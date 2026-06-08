def get_greeting(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Prompt user for name and print a greeting."""
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    print(get_greeting(name))


if __name__ == "__main__":
    main()
