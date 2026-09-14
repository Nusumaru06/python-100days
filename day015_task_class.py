# Day15 - Task Class

import datetime


class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.done = False

    def complete(self):
        # ここで完了状態にする
        self.done = True

    def is_overdue(self):
        due_date = datetime.datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        ).date()

        if not self.done and due_date < datetime.date.today():
            return True

        return False

task1 = Task(
    "Pythonを勉強する",
    3,
    "2026-09-20"
)

print(task1.title)
print(task1.priority)
print(task1.due_date)
print(task1.done)

print(task1.is_overdue())

task1.complete()

print(task1.done)
print(task1.is_overdue())

task2 = Task(
    "GitHubにpushする",
    1,
    "2026-09-30"
)

print(task2.title)
print(task2.priority)
print(task2.due_date)
print(task2.done)

print(task2.is_overdue())

def show_info(self):
    print(f"Title: {self.title}")
    print(f"Priority: {self.priority}")
    print(f"Due Date: {self.due_date}")
    print(f"Done: {self.done}")