import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added to the list.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{index}. {task['task']} [{status}]")

    def update_task(self, task_number, updated_task=None):
        if 0 < task_number <= len(self.tasks):
            if updated_task:
                self.tasks[task_number - 1]["task"] = updated_task
                print(f"Task {task_number} has been updated to: {updated_task}")
            else:
                self.tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" removed from the list.')
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

def menu():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.update_task(task_number)

        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            updated_task = input("Enter the new task description: ")
            todo_list.update_task(task_number, updated_task)

        elif choice == "5":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)

        elif choice == "6":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
            if confirm == 'y':
                todo_list.clear_tasks()

        elif choice == "7":
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    menu()
