#Class warmup

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.done = False

def complete(self):
    self.done = True

task1 = Task("Pythonを勉強する", 3)

print(task1.title)
print(task1.priority)
print(task1.done)