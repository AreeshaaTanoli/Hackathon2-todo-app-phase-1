import sys
from datetime import datetime

class Todo:
    """Represents a single task in the Todo list."""
    def __init__(self, task_id: int, title: str, deadline: str = None):
        self.id = task_id
        self.title = title
        self.creation_time = datetime.now()
        self.deadline = deadline
        self.status = "Incomplete"

    def __str__(self):
        status_symbol = "✓" if self.status == "Complete" else "✗"
        deadline_str = f" | Deadline: {self.deadline}" if self.deadline else ""
        created_str = self.creation_time.strftime("%Y-%m-%d %H:%M")
        return (
            f"[{status_symbol}] ID: {self.id} - {self.title}\n"
            f"    (Created: {created_str}{deadline_str} | Status: {self.status})"
        )

# In-memory storage for tasks
tasks = []
next_task_id = 1

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Todo List Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("----------------------")

def add_task():
    """Prompts the user for task details and adds it to the list."""
    global next_task_id
    title = input("Enter the task title: ")
    if not title:
        print("Task title cannot be empty.")
        return

    deadline = input("Enter a deadline (optional, e.g., '2025-12-31'): ")
    task = Todo(task_id=next_task_id, title=title, deadline=deadline or None)
    tasks.append(task)
    next_task_id += 1
    print(f"Task '{title}' added successfully.")

def view_tasks():
    """Displays all tasks currently in the list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        print(task)
    print("------------------")

def find_task_by_id(task_id: int) -> Todo | None:
    """Finds a task in the list by its ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def mark_task_complete():
    """Toggles a task's status between 'Incomplete' and 'Complete'."""
    try:
        task_id = int(input("Enter the task ID to toggle status: "))
        task = find_task_by_id(task_id)
        if task:
            if task.status == "Incomplete":
                task.status = "Complete"
            else:
                task.status = "Incomplete"
            print(f"Task {task_id} status changed to '{task.status}'.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

def update_task():
    """Updates the title or deadline of a specific task."""
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        new_title = input(f"Enter new title for task {task_id} (or press Enter to keep '{task.title}'): ")
        if new_title:
            task.title = new_title

        new_deadline_input = input(f"Enter new deadline for task {task_id} (e.g., '2025-12-31'), or type 'clear' to remove, or press Enter to keep current ('{task.deadline}'): ")
        if new_deadline_input.lower() == 'clear':
            task.deadline = None
        elif new_deadline_input:
            task.deadline = new_deadline_input
        
        print(f"Task {task_id} updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

def delete_task():
    """Deletes a specific task by its ID."""
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        task = find_task_by_id(task_id)
        if task:
            tasks.remove(task)
            print(f"Task {task_id} ('{task.title}') deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

def main():
    """Main function to run the Todo application loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting the Todo application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
