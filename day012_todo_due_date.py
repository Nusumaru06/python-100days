def input_due_date():
    while True:
        due = input("期限を入力してください (YYYY-MM-DD): ")

        try:
            datetime.strptime(due, "%Y-%m-%d")
            return due
        except ValueError:
            print("日付の形式が正しくありません。")