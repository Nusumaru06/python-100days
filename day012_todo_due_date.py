#ToDo_search
import json
import datetime

print("=== ToDo App v4.0 ===")


#メニューを表示
def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを検索")
    print("4 : タスクを完了")
    print("5 : タスクを削除")
    print("6 : 優先度順に表示")
    print("7 : 期限順に表示")
    print("8 : 終了")

#タスクを追加
def add_task(tasks):
    title = input("追加するタスクを入力してください: ")

    while True:
        print("優先度を選択してください")
        print("1 : Low")
        print("2 : Medium")
        print("3 : High")

        try:
            priority = int(input("選択: "))

            if priority in [1, 2, 3]:
                break
            else:
                print("1〜3を入力してください。")

        except ValueError:
            print("数字を入力してください。")

    new_task = {
        "title": title,
        "done": False,
        "priority": priority,
        "due_date": input_due_date()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"タスク '{title}' を追加しました。")

#タスクを検索
def search_tasks(tasks):
    keyword = input("検索するキーワードを入力してください: ")
    found_tasks = [
        task
        for task in tasks
        if keyword.lower() in task["title"].lower()
    ]
    if found_tasks:
        print(f"=== '{keyword}' を含むタスク一覧 ===")
        for i, task in enumerate(found_tasks, start=1):
            status = "x" if task["done"] else " "
            priority = task.get("priority", 0)
            print(f"{i}. [{status}] {task['title']} (優先度: {priority})")
    else:
        print(f"'{keyword}' を含むタスクは見つかりませんでした。")

#タスクのインデックスを取得
def get_task_index(tasks, message):
    if tasks:
        show_tasks(tasks)
        try:
            index = int(input(message)) - 1
            if 0 <= index < len(tasks):
                return index
            else:
                print("無効な番号です。")
        except ValueError:
            print("有効な番号を入力してください。")
    else:
        print("タスクはありません。")
    return None

#タスクを完了状態にする
def complete_task(tasks):
    index = get_task_index(tasks, "完了するタスクの番号を入力してください: ")
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"タスク '{tasks[index]['title']}' を完了しました。")

#タスクを削除
def delete_task(tasks):
    index = get_task_index(tasks, "削除するタスクの番号を入力してください: ")
    if index is not None:
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"タスク '{removed_task['title']}' を削除しました。")

#タスクを読み込む
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#jsonファイルにタスクを保存する
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

#タスク一覧を表示
def show_tasks(tasks):
    if tasks:
        print("=== タスク一覧 ===")

        priority_names = {
            3: "HIGH",
            2: "MEDIUM",
            1: "LOW",
            0: "NONE"
        }

        for i, task in enumerate(tasks, start=1):
            status = "x" if task["done"] else " "
            priority = task.get("priority", 0)
            priority_name = priority_names[priority]

            print(
                f"{i}. [{status}] [{priority_name}] "
                f"{task['title']} (期限: {task.get('due_date', 'なし')})"
            )
    else:
        print("タスクはありません。")

#優先度順に表示
def show_tasks_by_priority(tasks):
    if tasks:
        priority_names = {
            3: "HIGH",
            2: "MEDIUM",
            1: "LOW",
            0: "NONE"
        }

        sorted_tasks = sorted(
            tasks,
            key=lambda task: task.get("priority", 0),
            reverse=True
        )

        print("=== 優先度順のタスク一覧 ===")

        for i, task in enumerate(sorted_tasks, start=1):
            status = "x" if task["done"] else " "
            priority = task.get("priority", 0)
            priority_name = priority_names[priority]

            print(
                f"{i}. [{status}] [{priority_name}] "
                f"{task['title']}"
            )
    else:
        print("タスクはありません。")

#期限を入力
def input_due_date():
    while True:
        due_date = input("タスクの期限を入力してください (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            print("有効な日付を入力してください。例: 2026-09-22")

# 期限順に表示
def show_tasks_by_due_date(tasks):
    if tasks:
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task.get("due_date", "9999-12-31")
        )

        print("=== 期限順のタスク一覧 ===")

        priority_names = {
            3: "HIGH",
            2: "MEDIUM",
            1: "LOW",
            0: "NONE"
        }

        for i, task in enumerate(sorted_tasks, start=1):
            status = "x" if task["done"] else " "
            priority = task.get("priority", 0)
            priority_name = priority_names[priority]
            due_date = task.get("due_date", "なし")

            print(
                f"{i}. [{status}] [{priority_name}] "
                f"{task['title']} (期限: {due_date})"
            )
    else:
        print("タスクはありません。")

#初期化
tasks = load_tasks()

#メイン処理
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
        print("アプリを終了します。")
        break
    else:
        print("無効な選択です。")