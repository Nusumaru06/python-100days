# ToDo App v4.0

import json
import datetime

print("=== ToDo App v5.0 ===")


# メニューを表示
def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを検索")
    print("4 : タスクを完了")
    print("5 : タスクを削除")
    print("6 : 優先度順に表示")
    print("7 : 期限順に表示")
    print("8 : タスク統計")
    print("9 : 終了")


# タスクをJSONから読み込む
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# タスクをJSONへ保存
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=4
        )


# 期限を入力して日付形式を確認
def input_due_date():
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
            print(
                "有効な日付を入力してください。"
                "例: 2026-09-22"
            )


# タスクが期限切れか判定
def is_overdue(task):
    due_date_text = task.get("due_date")

    if not due_date_text:
        return False

    due_date = datetime.datetime.strptime(
        due_date_text,
        "%Y-%m-%d"
    ).date()

    return (
        due_date < datetime.date.today()
        and not task["done"]
    )


# 優先度名を取得
def get_priority_name(task):
    priority_names = {
        3: "HIGH",
        2: "MEDIUM",
        1: "LOW",
        0: "NONE"
    }

    priority = task.get("priority", 0)
    return priority_names.get(priority, "NONE")


# 1件のタスクを表示
def format_task(index, task):
    status = "x" if task["done"] else " "
    priority_name = get_priority_name(task)
    due_date = task.get("due_date", "なし")
    overdue_text = " [期限切れ]" if is_overdue(task) else ""

    return (
        f"{index}. [{status}] [{priority_name}] "
        f"{task['title']} "
        f"(期限: {due_date})"
        f"{overdue_text}"
    )


# タスク一覧を表示
def show_tasks(tasks):
    if not tasks:
        print("タスクはありません。")
        return

    print("=== タスク一覧 ===")

    for i, task in enumerate(tasks, start=1):
        print(format_task(i, task))


# タスクを追加
def add_task(tasks):
    title = input(
        "追加するタスクを入力してください: "
    )

    while True:
        print("優先度を選択してください")
        print("1 : Low")
        print("2 : Medium")
        print("3 : High")

        try:
            priority = int(input("選択: "))

            if priority in [1, 2, 3]:
                break

            print("1〜3を入力してください。")

        except ValueError:
            print("数字を入力してください。")

    due_date = input_due_date()

    new_task = {
        "title": title,
        "done": False,
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(
        f"タスク '{title}' を追加しました。"
    )


# タスクを検索
def search_tasks(tasks):
    keyword = input(
        "検索するキーワードを入力してください: "
    )

    found_tasks = [
        task
        for task in tasks
        if keyword.lower()
        in task["title"].lower()
    ]

    if not found_tasks:
        print(
            f"'{keyword}' を含むタスクは"
            "見つかりませんでした。"
        )
        return

    print(
        f"=== '{keyword}' を含むタスク一覧 ==="
    )

    for i, task in enumerate(
        found_tasks,
        start=1
    ):
        print(format_task(i, task))


# タスクのインデックスを取得
def get_task_index(tasks, message):
    if not tasks:
        print("タスクはありません。")
        return None

    show_tasks(tasks)

    try:
        index = int(input(message)) - 1

        if 0 <= index < len(tasks):
            return index

        print("無効な番号です。")

    except ValueError:
        print("有効な番号を入力してください。")

    return None


# タスクを完了状態にする
def complete_task(tasks):
    index = get_task_index(
        tasks,
        "完了するタスクの番号を"
        "入力してください: "
    )

    if index is None:
        return

    tasks[index]["done"] = True
    save_tasks(tasks)

    print(
        f"タスク '{tasks[index]['title']}' "
        "を完了しました。"
    )


# タスクを削除
def delete_task(tasks):
    index = get_task_index(
        tasks,
        "削除するタスクの番号を"
        "入力してください: "
    )

    if index is None:
        return

    removed_task = tasks.pop(index)
    save_tasks(tasks)

    print(
        f"タスク '{removed_task['title']}' "
        "を削除しました。"
    )


# 優先度順に表示
def show_tasks_by_priority(tasks):
    if not tasks:
        print("タスクはありません。")
        return

    sorted_tasks = sorted(
        tasks,
        key=lambda task: task.get("priority", 0),
        reverse=True
    )

    print("=== 優先度順のタスク一覧 ===")

    for i, task in enumerate(
        sorted_tasks,
        start=1
    ):
        print(format_task(i, task))


# 期限順に表示
def show_tasks_by_due_date(tasks):
    if not tasks:
        print("タスクはありません。")
        return

    sorted_tasks = sorted(
        tasks,
        key=lambda task: task.get(
            "due_date",
            "9999-12-31"
        )
    )

    print("=== 期限順のタスク一覧 ===")

    for i, task in enumerate(
        sorted_tasks,
        start=1
    ):
        print(format_task(i, task))


# タスク統計を表示
def show_task_statistics(tasks):
    total = len(tasks)

    completed = sum(
        1
        for task in tasks
        if task["done"]
    )

    incomplete = sum(
        1
        for task in tasks
        if not task["done"]
    )

    overdue = sum(
        1
        for task in tasks
        if is_overdue(task)
    )

    print("=== タスク統計 ===")
    print(f"総タスク数      : {total}")
    print(f"完了タスク数    : {completed}")
    print(f"未完了タスク数  : {incomplete}")
    print(f"期限超過タスク数: {overdue}")


# 初期化
tasks = load_tasks()


# メイン処理
while True:
    show_menu()
    choice = input("選択: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        search_tasks(tasks)
    elif choice == "4":
        complete_task(tasks)
    elif choice == "5":
        delete_task(tasks)
    elif choice == "6":
        show_tasks_by_priority(tasks)
    elif choice == "7":
        show_tasks_by_due_date(tasks)
    elif choice == "8":
        show_task_statistics(tasks)
    elif choice == "9":
        print("アプリを終了します。")
        break
    else:
        print("無効な選択です。")