#ランダムな文字を10文字出力
import random
import string

for i in range(10):
    char = random.choice(string.ascii_lowercase)
    print(char, end="")