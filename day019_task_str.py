#Day19_Tak_str_

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        status = "完了" if self.done else "未完了"
        return (
            f"[{status}]",
            f"{self.title}",
            f"(優先度: {self.priority})",
            f"(期限: {self.due_date})"
        )

task1 = Task(
    "pythonを学ぶ",
    "HIGH",
    "2026-09-25"
)

print(task1)