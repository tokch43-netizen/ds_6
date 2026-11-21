class task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.done = False


class taskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Додано")

    def remove_task(self, task):
        self.tasks.remove(task)
        print("Видалено")

    def complete_task(self, task):
        task.done = True
        print("Виконав/ла")

    def show_tasks(self):
        for task in self.tasks:
            print("Назва", task.name)
            print("Опис", task.description)
            print("Дедлайн", task.deadline)

            if task.done == True:
                print("Зробтв")
            else:
                print("Не зробив")


tasknumber1 = task("Закупи", "Закупити техніку", "21.11.26")
tasknumber2 = task("Реклама", "Зробити рекламу для магазину", "30.11.26")

manager = taskManager()

manager.add_task(tasknumber1)
manager.add_task(tasknumber2)

manager.complete_task(tasknumber1)

manager.show_tasks()