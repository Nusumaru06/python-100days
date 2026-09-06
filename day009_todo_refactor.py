#ToDo_refactoring
import json

print("=== ToDo App v2.5 ===")


#show_menu関数
def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを完了")
    print("4 : タスクを削除")
    print("5 : 終了")

#show_tasks関数
def show_tasks(tasks):
    if tasks:
        print("=== タスク一覧 ===")
        for i, task in enumerate(tasks, start=1):
            status = "x" if task["done"] else " "
            print(f"{i}. [{status}] {task['title']}")
    else:
        print("タスクはありません。")

#add_tasks関数
def add_task(tasks):
    title = input("追加するタスクを入力してください: ")

    new_task = {
        "title": title,
        "done": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"タスク '{title}' を追加しました。")

#complete_task関数
def complete_task(tasks):
    if tasks:
        show_tasks(tasks)
        try:
            index = int(input("完了するタスクの番号を入力してください: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
                print(f"タスク '{tasks[index]['title']}' を完了しました。")
            else:
                print("無効な番号です。")
        except ValueError:
            print("有効な番号を入力してください。")
    else:
        print("タスクはありません。")

#delete_task関数
def delete_task(tasks):
    if tasks:
        show_tasks(tasks)
        try:
            index = int(input("削除するタスクの番号を入力してください: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"タスク '{removed_task['title']}' を削除しました。")
            else:
                print("無効な番号です。")
        except ValueError:
            print("有効な番号を入力してください。")
    else:
        print("タスクはありません。")

#load_tasks関数
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#save_tasks関数
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
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("アプリを終了します。")
        break

    else:
        print("無効な選択です。")