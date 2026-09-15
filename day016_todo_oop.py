# Day16 - OOP ToDo App

import datetime


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


tasks = []


def show_menu():
    print("\n1 : タスクを追加")
    print("2 : タスク一覧")
    print("3 : タスクを完了")
    print("4 : タスクを削除")
    print("5 : 終了")


def add_task(tasks):
    # ここで title / priority / due_date を入力
    # Task(...) を作って tasks に追加する
    ...


def show_tasks(tasks):
    # Taskオブジェクトの属性を使って一覧表示
    ...


def complete_task(tasks):
    # 番号を受け取って tasks[index].complete()
    ...


def delete_task(tasks):
    # 番号を受け取って pop()
    ...


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