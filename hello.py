"""用Python设计第一个游戏"""

t = input("不妨猜一下小珊子现在心里想的是哪个数字（0-10范围内的整数）：")
guess = int(t)

if guess == 3:
    print("嘻嘻嘻，对着呢对着呢！")
    print("爱你哟！")
else:
    print("哎呀呀，错误！")

print("Game Over!")


