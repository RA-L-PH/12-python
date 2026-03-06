todos = []

def show_todos():
    if not todos:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def add_task(task):
    todos.append(task)
    print(f'Added: "{task}"')

def remove_task(index):
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        print(f'Removed: "{removed}"')
    else:
        print("Invalid task number.")

print("To-Do List App")
while True:
    print("\n1. Show tasks\n2. Add task\n3. Remove task\n4. Quit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        show_todos()
        if todos:
            try:
                num = int(input("Enter task number to remove: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            remove_task(num)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
