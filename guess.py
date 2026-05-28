# -*- coding: utf-8 -*-
import random

secret = random.randint(1, 100)
attempts = 0

print("猜数字游戏！范围 1-100")

while True:
    guess = int(input("请输入你的猜测: "))
    attempts += 1

    if guess < secret:
        print("太小了！")
    elif guess > secret:
        print("太大了！")
    else:
        print(f"恭喜你猜对了！用了 {attempts} 次。")
        break
