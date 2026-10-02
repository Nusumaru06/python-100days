import datetime
import json

from task import Task

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

    def input_priority(self):
        while True:
            priority = input(
                "タスクの優先度を入力してください (高, 中, 低): "
            )

            if priority in ["高", "中", "低"]:
                return priority

            print("有効な優先度を入力してください。")

    def input_due_date(self):
        while True:
            due_date = input(
                "タスクの期限を入力してください (YYYY-MM-DD): "
            )

            try:
                datetime.datetime.strptime(
                    due_date,
                    "%Y-%m-%d"
                )
                return due_date

            except ValueError:
                print("有効な日付を入力してください。")

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
            self.save_tasks()

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
        keyword = input("検索キーワードを入力してください: ")

        found_tasks = [
            task
            for task in self.tasks
            if keyword.lower() in task.title.lower()
        ]

        if not found_tasks:
            print("該当するタスクはありません。")
            return

        print("=== 検索結果 ===")

        for i, task in enumerate(found_tasks, start=1):
            print(f"{i}. {task}")

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
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.done)
        incomplete = sum(1 for task in self.tasks if not task.done)
        overdue = sum(1 for task in self.tasks if task.is_overdue())

        print("=== タスク統計 ===")
        print(f"総タスク数: {total}")
        print(f"完了: {completed}")
        print(f"未完了: {incomplete}")
        print(f"期限切れ: {overdue}")

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]

        with open(
            "task_manager.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load_tasks(self):
        try:
            with open(
                "task_manager.json",
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            return [
                Task.from_dict(task_data)
                for task_data in data
            ]

        except FileNotFoundError:
            return []

    def run(self):
        while True:
            self.show_menu()

            choice = input("選択: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.show_tasks()

            elif choice == "3":
                self.search_tasks()

            elif choice == "4":
                self.complete_task()

            elif choice == "5":
                self.delete_task()

            elif choice == "6":
                self.show_statistics()

            elif choice == "7":
                print("アプリを終了します。")
                break

            else:
                print("無効な選択です。")


app = TodoApp()
app.run()