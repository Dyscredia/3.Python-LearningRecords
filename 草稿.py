time = input("这是一个电子时钟显示器。请输入一个24小时制的时间（格式示例：1824）：")
list_num = []
for each in str(time):
    x = int(each)
    list_num.append(x)
print(list_num)