class Task():

    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status


    def mark_as_completed(self):
        self.status = True

    def __str__(self):
        status_str = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок выполнения: {self.due_date}, Статус: {status_str}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Задача '{task.description}' добавлена. Срок выполнения: {task.due_date}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()  # Отмечаем задачу как выполненную
            print(f"Задача '{self.tasks[task_index].description}' помечена как выполненная.")

    def list_current_tasks(self):
        print("Текущие задачи (не выполненные):")
        for task in self.tasks:
            if not task.status:
                print(task)


task_manager = TaskManager()
task1 = Task("Закончить отчет", "12.01.2025")
task_manager.add_task(task1)

task2 = Task("Подготовить презентацию", "15.01.2025")
task_manager.add_task(task2)

task_manager.list_current_tasks() # Список текущих задач

task_manager.mark_task_completed(0) # Отмечаем первую задачу как выполненную

task_manager.list_current_tasks() # Список текущих задач после выполнения