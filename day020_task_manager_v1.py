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
            title = input(
                "追加するタスクを入力してください"
            )

            priority = self.input_priority()
            due_date = self.input_due_date()

            new_task = Task(
                title,
                priority,
                due_date
            )

            self.tasks.append(new_task)

            print(
                f"タスク '{title}' を追加しました。"
            )

    def show_tasks(self):
        if not self.tasks:
            print("タスクはありません。")
            return

        print("=== タスク一覧 ===")

        for i, task in enumerate(
            self.tasks,
            start=1
        ):
            status = "x" if task.done else " "

            print(
                f"{i}. "
                f"[{status}] "
                f"{task.title} "
                f"(優先度: {task.priority}) "
                f"(期限: {task.due_date})"
            )

    def get_task_index(self, message):
        if not self.tasks:
            print("タスクはありません。")
            return None

        self.show_tasks()

        try:
            index = int(input(message)) - 1

            if 0 <= index < len(self.tasks):
                return index

            print("無効な番号です。")

        except ValueError:
            print("有効な番号を入力してください。")

        return None

    def search_tasks(self):
        ...

    def complete_task(self):
        index = self.get_task_index(
            "完了するタスクの番号を入力してください: "
        )

        if index is None:
            return

        self.tasks[index].complete()
        self.save_tasks()

        print(
            f"タスク "
            f"'{self.tasks[index].title}' "
            f"を完了しました。"
        )

    def delete_task(self):
        index = self.get_task_index(
            "削除するタスクの番号を入力してください: "
        )

        if index is None:
            return

        removed_task = self.tasks.pop(index)
        self.save_tasks()

        print(
            f"タスク "
            f"'{removed_task.title}' "
            f"を削除しました。"
        )

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