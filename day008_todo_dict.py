#ToDo App v2.0
print("=== ToDo App v2.0 ===")

import json

def load_tasks():
    try:
        with open("todo.json", "r", encoding = "utf-8") as file:
            #jsonを読み込む
            return json.load(file)
    # JSONファイルが存在しない初回起動時は、空のタスクリストを返す
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("todo.json", "w", encoding = "utf-8") as file:
        #jsonに書き込む
        json.dump(tasks, file, ensure_ascii=False, indent=4)

#初期化
tasks = load_tasks()

#処理を選択
while True:
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを完了")
    print("4 : タスクを削除")
    print("5 : 終了")

    choice = input("選択: ")

#タスクの追加
    if choice == "1":
        title = input("追加するタスクを入力してください: ")

        new_task = {
            "title": title,
            "done": False
        }

        tasks.append(new_task)
        save_tasks(tasks)
        print(f"タスク '{title}' を追加しました。")

#タスクの一覧表示
    elif choice == "2":
        if tasks:
            print("=== タスク一覧 ===")
            for i, task in enumerate(tasks, start=1):
                status = "x" if task["done"] else " "
                print(f"{i}. [{status}] {task['title']}")
        else:
            print("タスクはありません。")

#タスクの完了
    elif choice == "3":
        if tasks:
            print("=== タスク一覧 ===")
            for i, task in enumerate(tasks, start=1):
                status = "x" if task["done"] else " "
                print(f"{i}. [{status}] {task['title']}")
            try:
                # ユーザーは1番から入力するが、Pythonのリストは0番から始まるため1を引く
                index = int(input("完了するタスクの番号を入力してください: ")) - 1
                if 0 <= index < len(tasks):
                    # タスクの完了状態だけ変更し、タスク自体は削除しない
                    tasks[index]["done"] = True
                    save_tasks(tasks)
                    print(f"タスク '{tasks[index]['title']}' を完了しました。")
                else:
                    print("無効な番号です。")
            except ValueError:
                print("有効な番号を入力してください。")
        else:
            print("タスクはありません。")

#タスクの削除
    elif choice == "4":
        if tasks:
            print("=== タスク一覧 ===")
            for i, task in enumerate(tasks, start=1):
                status = "x" if task["done"] else " "
                print(f"{i}. [{status}] {task['title']}")
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

#アプリの終了
    elif choice == "5":
        print("アプリを終了します。")
        break
    else:
        print("無効な選択です。")