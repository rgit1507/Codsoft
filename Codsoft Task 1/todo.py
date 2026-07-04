import json
import os

# File to store the to-do list data
FILE_NAME = 'todo_list.json'

def load_tasks():
    """Loads tasks from the JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Displays all tasks with their current status."""
    print("\n" + "="*30)
    print("       📋 MY TO-DO LIST")
    print("="*30)
    
    if not tasks:
        print("No tasks found! You are all caught up.")
    else:
        for index, task in enumerate(tasks, 1):
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{index}. {status} {task['name']}")
    print("="*30)

def add_task(tasks):
    """Adds a new task to the list."""
    task_name = input("Enter the new task description: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"\n✅ Task '{task_name}' added successfully!")
        save_tasks(tasks)
    else:
        print("\n❌ Task name cannot be empty.")

def update_task(tasks):
    """Updates the description of an existing task."""
    display_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Enter the new task description: ").strip()
            if new_name:
                tasks[task_num - 1]['name'] = new_name
                print("\n✅ Task updated successfully!")
                save_tasks(tasks)
            else:
                print("\n❌ Task name cannot be empty.")
        else:
            print("\n❌ Invalid task number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def mark_completed(tasks):
    """Marks a pending task as completed."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("\n✅ Task marked as completed!")
            save_tasks(tasks)
        else:
            print("\n❌ Invalid task number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"\n🗑️ Task '{removed_task['name']}' deleted!")
            save_tasks(tasks)
        else:
            print("\n❌ Invalid task number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def main():
    """Main menu loop for the application."""
    tasks = load_tasks()
    
    while True:
        display_tasks(tasks)
        print("\nMain Menu:")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Mark Task as Completed")
        print("4. Delete a Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\n👋 Goodbye! Have a productive day.")
            break
        else:
            print("\n❌ Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()