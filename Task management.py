class Task:
    def __init__(self, title, description, due_date, assigned_to, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, due_date, assigned_to):
        task = Task(title, description, due_date, assigned_to)
        self.tasks.append(task)

    def update_task(self, task_index, title, description, due_date, assigned_to):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.title = title
            task.description = description
            task.due_date = due_date
            task.assigned_to = assigned_to
        else:
            print("Task not found")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True
        else:
            print("Task not found")

    def mark_task_incomplete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = False
        else:
            print("Task not found")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Task not found")

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"Task {index}:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Assigned To: {task.assigned_to}")
            print(f"Status: {'Completed' if task.completed else 'Incomplete'}")
            print()


def main():
    task_manager = TaskManager()

    while True:
        print("Task Management System")
        print("1. Create Task")
        print("2. Update Task")
        print("3. Mark Task as Complete")
        print("4. Mark Task as Incomplete")
        print("5. Delete Task")
        print("6. List Tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            assigned_to = input("Enter assigned user: ")
            task_manager.create_task(title, description, due_date, assigned_to)
        elif choice == "2":
            task_manager.list_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            due_date = input("Enter new due date: ")
            assigned_to = input("Enter new assigned user: ")
            task_manager.update_task(task_index, title, description, due_date, assigned_to)
        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Enter the index of the task to mark as complete: "))
            task_manager.mark_task_complete(task_index)
        elif choice == "4":
            task_manager.list_tasks()
            task_index = int(input("Enter the index of the task to mark as incomplete: "))
            task_manager.mark_task_incomplete(task_index)
        elif choice == "5":
            task_manager.list_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            task_manager.delete_task(task_index)
        elif choice == "6":
            task_manager.list_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()