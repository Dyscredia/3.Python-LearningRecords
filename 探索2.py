print("数字炸弹游戏开始啦！请每轮输入一个数字，我将告诉你它与炸弹数的关系。",
      "看看你能多少轮猜出炸弹~\n我们的炸弹范围是[0,100]，且为整数。每轮猜测请输入不同数字~")
import random
x = random.randint(0,100)
times = 6
while times > 0:
    A = input("请猜测：")
    M = int(A)
    if M == x:
        print("猜对啦！你真棒~")
        break
    else:
        if M < x:
            print("太小啦！往大了猜")
        else:
            print("太大啦！往小了猜")
    times = times - 1
    print("剩余机会：" ,times)
if times == 6:
    print("一次就中，夸夸！")
if times == 0:
    print("大笨蛋，不和你玩了")
print("游戏结束啦~")