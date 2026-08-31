#じゃんけんゲーム
print("== じゃんけんゲーム ==")
print("1 : グー")
print("2 : チョキ")
print("3 : パー")

#プレイヤーの手を取得
def player_hand():
    choice = int(input("選択してください: "))
    if choice == 1:
        return "グー"
    elif choice == 2:
        return "チョキ"
    elif choice == 3:
        return "パー"
player = player_hand()

#cpuの手を取得
def cpu_hand():
    import random
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        return "グー"
    elif cpu_choice == 2:
        return "チョキ"
    elif cpu_choice == 3:
        return "パー"
cpu = cpu_hand()


#勝敗の判定
def judge(player_hand, cpu_hand):
    if player_hand == cpu_hand:
        return "引き分け"
    elif (player_hand == "グー" and cpu_hand == "チョキ") or (player_hand == "チョキ" and cpu_hand == "パー") or (player_hand == "パー" and cpu_hand == "グー"):
        return "あなたの勝ち"
    else:
        return "CPUの勝ち"
result = judge(player, cpu)

#結果を表示
print(f"あなたの手は{player}で相手の手は{cpu}だったので{result}です")