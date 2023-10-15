import json

# Define the filename for storing tasks
TODO_FILE = "tasks.json"

# Initialize an empty list to store tasks
tasks = []

# Load tasks from the JSON file if it exists
try:
    with open(TODO_FILE, "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

# Function to save tasks to the JSON file
def save_tasks():
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task(title, description):
    task = {"title": title, "description": description, "done": False}
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['title']} ({status})")

# Function to mark a task as done
def mark_task_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks()
        print("Task marked as done!")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to mark as done: ")) - 1
        mark_task_done(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

