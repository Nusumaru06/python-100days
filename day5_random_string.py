#Random String Generator
import random
import string

#生成する文字数の決定
print("=== Random String Generator ===")
length = int(input("生成する文字数を入力してください: "))

#大文字を含めるかの選択
def choice_1():
    while True:
        choice1 = input("大文字を含めますか？ (y/n): ")
        if choice1 == "y":
            return 1
        elif choice1 == "n":
            return 2
        else:
            print("無効な入力です。")
upper_choice = choice_1()

#数字を含めるかの選択
def choice_2():
    while True:
        choice2 = input("数字を含めますか？ (y/n): ")
        if choice2 == "y":
            return 1
        elif choice2 == "n":
            return 2
        else:
            print("無効な入力です。")
digit_choice = choice_2()

#文字プールの作成
if upper_choice == 1 and digit_choice == 1:
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits

elif upper_choice == 1 and digit_choice == 2:
    pool = string.ascii_lowercase + string.ascii_uppercase

elif upper_choice == 2 and digit_choice == 1:
    pool = string.ascii_lowercase + string.digits

else:
    pool = string.ascii_lowercase

#文字列の生成
result = "".join(random.choices(pool, k = length))

#結果の表示
print(f"生成されたランダムな文字列は{length}文字で{result}です。")