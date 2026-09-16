#OOP Json ToDo App

import datetime

print("=== OOP Json ToDo App ===")


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

    def get_priority_name(self):
        priority_names = {
            3: "HIGH",
            2: "MEDIUM",
            1: "LOW"
        }

        return priority_names.get(
            self.priority,
            "NONE"
        )


def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを完了")
    print("4 : タスクを削除")
    print("5 : 終了")


def input_priority():
    while True:
        print("優先度を選択してください")
        print("1 : Low")
        print("2 : Medium")
        print("3 : High")

        try:
            priority = int(input("選択: "))

            if priority in [1, 2, 3]:
                return priority

            print("1〜3を入力してください。")

        except ValueError:
            print("数字を入力してください。")


def input_due_date():
    while True:
        due_date = input(
            "期限を入力してください "
            "(YYYY-MM-DD): "
        )

        try:
            datetime.datetime.strptime(
                due_date,
                "%Y-%m-%d"
            )

            return due_date

        except ValueError:
            print(
                "正しい日付を入力してください。"
            )


def add_task(tasks):
    title = input(
        "追加するタスクを入力してください: "
    )

    priority = input_priority()
    due_date = input_due_date()

    new_task = Task(
        title,
        priority,
        due_date
    )

    tasks.append(new_task)

    print(
        f"タスク '{title}' を追加しました。"
    )


def show_tasks(tasks):
    if not tasks:
        print("タスクはありません。")
        return

    print("=== タスク一覧 ===")

    for i, task in enumerate(
        tasks,
        start=1
    ):
        status = "x" if task.done else " "

        overdue_text = (
            " [期限切れ]"
            if task.is_overdue()
            else ""
        )

        print(
            f"{i}. "
            f"[{status}] "
            f"[{task.get_priority_name()}] "
            f"{task.title} "
            f"(期限: {task.due_date})"
            f"{overdue_text}"
        )


def get_task_index(tasks, message):
    if not tasks:
        print("タスクはありません。")
        return None

    show_tasks(tasks)

    try:
        index = int(
            input(message)
        ) - 1

        if 0 <= index < len(tasks):
            return index

        print("無効な番号です。")

    except ValueError:
        print(
            "有効な番号を入力してください。"
        )

    return None


def complete_task(tasks):
    index = get_task_index(
        tasks,
        "完了するタスクの番号を"
        "入力してください: "
    )

    if index is None:
        return

    tasks[index].complete()

    print(
        f"タスク "
        f"'{tasks[index].title}' "
        f"を完了しました。"
    )


def delete_task(tasks):
    index = get_task_index(
        tasks,
        "削除するタスクの番号を"
        "入力してください: "
    )

    if index is None:
        return

    removed_task = tasks.pop(index)

    print(
        f"タスク "
        f"'{removed_task.title}' "
        f"を削除しました。"
    )

tasks = []

while True:
    show_menu()

    choice = input("選択: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("アプリを終了します。")
        break
    else:
        print("無効な選択です。")