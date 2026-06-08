todos = []


def show_todos():
    if not todos:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todos, 1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")


def add_task(task):
    if not task or not task.strip():
        print("Task cannot be empty.")
        return
    task = task.strip()
    todos.append({"task": task, "completed": False})
    print(f'Added: "{task}"')


def remove_task(index):
    if not todos:
        print("No tasks to remove.")
        return
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        print(f'Removed: "{removed["task"]}"')
    else:
        print(f"Invalid task number. Choose between 1 and {len(todos)}.")


def mark_complete(index):
    if not todos:
        print("No tasks to mark complete.")
        return
    if 1 <= index <= len(todos):
        task = todos[index - 1]
        if task["completed"]:
            print(f'Task "{task["task"]}" is already completed.')
        else:
            task["completed"] = True
            print(f'Completed: "{task["task"]}"')
    else:
        print(f"Invalid task number. Choose between 1 and {len(todos)}.")


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


print("To-Do List App")
while True:
    print("\n1. Show tasks\n2. Add task\n3. Remove task\n4. Quit\n5. Mark task complete")
    choice = input("Choose (1-5): ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        show_todos()
        if todos:
            num = read_int("Enter task number to remove: ")
            if num is not None:
                remove_task(num)
    elif choice == "4":
        print("Goodbye!")
        break
    elif choice == "5":
        show_todos()
        if todos:
            num = read_int("Enter task number to mark complete: ")
            if num is not None:
                mark_complete(num)
    else:
        print("Invalid choice. Choose between 1 and 5.")
