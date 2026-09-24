import datetime


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

    def input_priority(self):
        while True:
            print("優先度を選択してください")
            print("1 : Low")
            print("2 : Medium")
            print("2 : High")

            try:
                priority = int(input("選択: "))

                if priority in [1, 2, 3]:
                    return priority

                print("1~3を入力してください")

            except ValueError:
                print("数字を入力してください")

    def input_due_date(self):
        while True:
            due_date = input(
                "期限を入力してください"
                "(YYYY-MM-DD): "
            )

            try:
                datetime.datetime.fromisoformat(due_date)
                return due_date


                return due_date

            except ValueError:
                print(
                    "正しい日付を入力してください"
                )

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

    def complete_task(self):
        index = self.get_task_index(
            "完了するタスクの番号を入力してください: "
        )

        if index is None:
            return

        self.tasks[index].complete()

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

        print(
            f"タスク "
            f"'{removed_task.title}' "
            f"を削除しました。"
        )

    def run(self):
        while True:
            self.show_menu()

            choice = input("選択: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.show_tasks()

            elif choice == "3":
                self.complete_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                print("アプリを終了します。")
                break

            else:
                print("無効な選択です。")


app = TodoApp()
app.run()