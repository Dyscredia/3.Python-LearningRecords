time = input("这是一个电子时钟显示器。请输入一个时间，用连续的四位数表示（示例：1824）：")
list_num = []
for each in str(time):
    x = int(each)
    list_num.append(x)
print(list_num)