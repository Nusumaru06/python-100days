# Day20 - Mini Capstone
# Task Manager v1.0

import datetime
import json


class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.done = False

    def complete(self):
        self.done = True

    def is_overdue(self):
        due_date = datetime.datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        ).date()

        return (
            not self.done
            and due_date < datetime.date.today()
        )

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["priority"],
            data["due_date"]
        )

        task.done = data.get("done", False)

        return task

    def __str__(self):
        status = "完了" if self.done else "未完了"

        return (
            f"[{status}]",
            f"{self.title}",
            f"(優先度: {self.priority})",
            f"(期限: {self.due_date})"
        )


class TodoApp:
    def __init__(self):
        self.tasks = self.load_tasks()

    def show_menu(self):
        print("\n=== Task Manager v1.0 ===")
        print("1 : タスクを追加")
        print("2 : タスク一覧")
        print("3 : タスクを検索")
        print("4 : タスクを完了")
        print("5 : タスクを削除")
        print("6 : タスク統計")
        print("7 : 終了")

    def add_task(self):
        ...

    def show_tasks(self):
        ...

    def search_tasks(self):
        ...

    def complete_task(self):
        ...

    def delete_task(self):
        ...

    def show_statistics(self):
        ...

    def save_tasks(self):
        ...

    def load_tasks(self):
        ...

    def run(self):
        ...


app = TodoApp()
app.run()