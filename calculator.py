#電卓アプリ
print("=== 電卓アプリ ===")
print("1 : 足し算")
print("2 : 引き算")
print("3 : 掛け算")
print("4 : 割り算")

choice = input("選んでください: ")

data1 = float(input("1つ目の数字:  "))
data2 = float(input("2つ目の数字:  "))

result = None
if choice == "1":
    result = data1 + data2
    print(f"結果:{data1} + {data2} = {result}")

elif choice == "2":
    result = data1 - data2
    print(f"結果:{data1} - {data2} = {result}")

elif choice == "3":
    result = data1 * data2
    print(f"結果:{data1} * {data2} = {result}")

elif choice == "4":

    if data2 == 0:
        print("0で割ることはできません")
    else:
        result = data1 / data2
        print(f"結果:{data1} / {data2} = {result}")

else:
    print("無効な選択です")