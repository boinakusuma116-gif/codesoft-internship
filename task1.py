import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"task": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['task']} [{status}]")

# Update task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task: ")
            tasks[index]["task"] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

# Mark task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_complete(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
