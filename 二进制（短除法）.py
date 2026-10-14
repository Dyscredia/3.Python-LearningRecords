x = input("请输入任意一个正整数：")
XX_10 = int(x)
list = []
while XX_10 != 0:
    YU = XX_10 % 2
    list.append(str(YU))
    XX_10 = XX_10 // 2
list.reverse()
nums_2 = ''.join(list)
result_2 = int(nums_2)
print(result_2)