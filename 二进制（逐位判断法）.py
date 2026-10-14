x = input("请输入一个正整数：")
G = int(x)
list0 = []
i = 0
while 2 ** i <= G:
    i += 1
i = i - 1
list0.append(str(1))
P = 2 ** i
M = i - 1
while M >= 0:
    if P + 2 ** M > G:
        list0.append(str(0))
    else:
        list0.append(str(1))
        P = P + 2 ** M
    M -= 1
print("转换为二进制数：" + "".join(list0))