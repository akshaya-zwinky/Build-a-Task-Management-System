from datetime import datetime

# ...

class TaskManager:
    # ... (previous methods)

    def search_tasks(self, query):
        matching_tasks = []
        for task in self.tasks:
            if (
                query in task.title
                or query in task.description
                or query == task.assigned_to
            ):
                matching_tasks.append(task)
        return matching_tasks

    def filter_tasks(self, completed=None, due_date=None):
        filtered_tasks = []
        for task in self.tasks:
            if (
                (completed is None or task.completed == completed)
                and (due_date is None or self._is_due_date_within_range(task, due_date))
            ):
                filtered_tasks.append(task)
        return filtered_tasks

    def _is_due_date_within_range(self, task, due_date):
        if not task.due_date:
            return False
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            task_due_date_obj = datetime.strptime(task.due_date, "%Y-%m-%d")
            return task_due_date_obj <= due_date_obj
        except ValueError:
            return False

# ...

def main():
    task_manager = TaskManager()

    while True:
        # ... (previous menu options)

        elif choice == "8":
            query = input("Enter search query (title, description, or user): ")
            matching_tasks = task_manager.search_tasks(query)
            if matching_tasks:
                print("Matching tasks:")
                for index, task in enumerate(matching_tasks):
                    print(f"Task {index}: {task.title}")
            else:
                print("No matching tasks found.")
        elif choice == "9":
            completed_filter = input("Filter by completion (completed, incomplete, or all): ").lower()
            due_date_filter = input("Filter by due date (YYYY-MM-DD or leave empty): ")
            if completed_filter not in ["completed", "incomplete", "all"]:
                print("Invalid completion filter. Please use 'completed', 'incomplete', or 'all'.")
                continue
            filtered_tasks = task_manager.filter_tasks(
                completed=(None if completed_filter == "all" else completed_filter == "completed"),
                due_date=due_date_filter,
            )
            if filtered_tasks:
                print("Filtered tasks:")
                for index, task in enumerate(filtered_tasks):
                    print(f"Task {index}: {task.title}")
            else:
                print("No tasks match the specified filters.")