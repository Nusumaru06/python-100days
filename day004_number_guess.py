#数字当てゲーム

print("=== 数字当てゲーム ===")
print("1から100までの数字を当ててください。")

#難易度選択
print("1 * Easy")
print("2 * Normal")
print("3 * Hard")

while True:
    difficulty = int(input("難易度を選択してください: "))
    if difficulty in [1, 2, 3]:
        break
    else:
        print("無効な選択です。1, 2, または 3 を選んでください。")

#試行回数を決定
def choose_difficulty():
    if difficulty == 1:
        return 10

    elif difficulty == 2:
        return 7

    elif difficulty == 3:
        return 5

attempts = choose_difficulty()

#答えを生成
import random

def generate_answer():
    return random.randint(1, 100)
answer = generate_answer()

#ゲームの実行処理

def play_game():
    count = 1

    while count <= attempts:
        print(f"残りの試行回数: {attempts - count + 1}")
        guess = int(input("予想: "))

        if guess < 1 or guess > 100:
            print("1から100までの数字を入力してください。")
            continue

        if guess == answer:
            return 1
        elif guess < answer:
            print("もっと大きな数です。")
        else:
            print("もっと小さな数です。")
        count += 1
    if count > attempts:
        return 2

result = play_game()

#結果の表示
if result == 1:
    print(f"おめでとうございます！正解は {answer} です。")
elif result == 2:
    print(f"残念でした。正解は {answer} でした。")

