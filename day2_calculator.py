#電卓アプリ
#計算方法をユーザーが選択
print("=== 電卓アプリ ===")
print("1 : 足し算")
print("2 : 引き算")
print("3 : 掛け算")
print("4 : 割り算")

choice = input("選んでください: ")

#数字を入力
num1 = float(input("1つ目の数字:  "))
num2 = float(input("2つ目の数字:  "))

#計算処理と結果の表示
result = None
if choice == "1":
    result = num1 + num2
    print(f"結果:{num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"結果:{num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"結果:{num1} * {num2} = {result}")

elif choice == "4":

    if num2 == 0:
        print("0で割ることはできません")
    else:
        result = num1 / num2
        print(f"結果:{num1} / {num2} = {result}")

else:
    print("無効な選択です")