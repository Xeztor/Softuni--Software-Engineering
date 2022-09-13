class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        all_task_names = self.get_all_task_names()
        if task_name not in all_task_names:
            return f"Could not find task with the name {task_name}"
        else:
            task = self.get_task_by_name(task_name)
            task.completed = True
            return f"Completed task {task_name}"

    def clean_section(self):
        to_be_removed = []
        for task in self.tasks:
            if task.completed:
                to_be_removed.append(task)

        for i in range(len(to_be_removed)):
            self.tasks.remove(to_be_removed[i])
        return f"Cleared {len(to_be_removed)} tasks."

    def view_section(self):
        tasks_detail = [task.details() for task in self.tasks]
        return f"Section {self.name}:\n" + '\n'.join(tasks_detail)

    def get_task_by_name(self, task_name):
        for task in self.tasks:
            if task.username == task_name:
                return task

    def get_all_task_names(self):
        return [task.username for task in self.tasks]
