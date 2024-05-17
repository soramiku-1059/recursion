import random

n = input("最小値を入力してください_")
m = input("最大値をに入力してください_")

x = random.randint(int(n),int(m))

for i in range(10):
    inNumber = input("数を入力してください")
    if x == int(inNumber):
        print("正解")
        break
    if i == 9:
        print("不正解 数は" + str(x) + "でした")