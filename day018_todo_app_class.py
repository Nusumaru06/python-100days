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


class TodoApp:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n1 : タスクを追加")
        print("2 : タスク一覧")
        print("3 : タスクを完了")
        print("4 : タスクを削除")
        print("5 : 終了")