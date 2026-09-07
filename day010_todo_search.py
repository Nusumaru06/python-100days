#ToDo_search
import json

print("=== ToDo App v3.0 ===")


#メニューを表示
def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを検索")
    print("4 : タスクを完了")
    print("5 : タスクを削除")
    print("6 : 終了")

#タスク一覧を表示
def show_tasks(tasks):
    if tasks:
        print("=== タスク一覧 ===")
        for i, task in enumerate(tasks, start=1):
            status = "x" if task["done"] else " "
            print(f"{i}. [{status}] {task['title']}")
    else:
        print("タスクはありません。")

#タスクを追加
def add_task(tasks):
    title = input("追加するタスクを入力してください: ")

    new_task = {
        "title": title,
        "done": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"タスク '{title}' を追加しました。")

#タスクを検索
def search_tasks(tasks):
    keyword = input("検索するキーワードを入力してください: ")
    found_tasks = [task for task in tasks if keyword in task["title"]]

    if found_tasks:
        print(f"=== '{keyword}' を含むタスク一覧 ===")
        for i, task in enumerate(found_tasks, start=1):
            status = "x" if task["done"] else " "
            print(f"{i}. [{status}] {task['title']}")
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
        print("アプリを終了します。")
        break
    else:
        print("無効な選択です。")