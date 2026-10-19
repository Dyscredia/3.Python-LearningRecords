# 模拟电子时钟显示器，我们画出初步的点位全览图，列数53，行数21。从0开始对每个点位编号。
# 暂时先用数字序列标记此1113个点位的开关情况，初始状态均为0。后续将开关打开的点位替换为1，打印输出时再做排版。
list_total = [0] * 1113  

list_switches = [  # 我们需要显示数字0-9，7个笔画分别用7个开关来控制，1则显示此笔画，0则留空。建立开关总表。
    [1, 1, 1, 0, 1, 1, 1], #0
    [0, 0, 1, 0, 0, 1, 0], #1
    [1, 0, 1, 1, 1, 0, 1], #2
    [1, 0, 1, 1, 0, 1, 1], #3
    [0, 1, 1, 1, 0, 1, 0], #4
    [1, 1, 0, 1, 0, 1, 1], #5
    [1, 1, 0, 1, 1, 1, 1], #6
    [1, 0, 1, 0, 0, 1, 0], #7
    [1, 1, 1, 1, 1, 1, 1], #8
    [1, 1, 1, 1, 0, 1, 1], #9
    ]

# 我们需要在大坐标图上预先找出每个笔画开关涉及到的点位，后续可以直接据此修改大图中将相应点位的取值。
# 以下列表名称均带有两个数字编号，前者取0-3，代表turn（四位数时间中的哪一位），后者取0-6，代表order（7个开关中的哪一个）。
# 所有横画的形状都是一致的，编号总体发生改变。类推得到四位数时间中每个数、每个轮次涉及到的点位，分别建立开关的占位编号序列。
list00 = [2, 3, 4, 5, 6, 7, 8, 
          54, 55, 56, 57, 58, 59, 60, 61, 62, 
          108, 109, 110, 111, 112, 113, 114]
list10 = []
list20 = []
list30 = []
list03 = []
list13 = []
list23 = []
list33 = []
list06 = []
list16 = []
list26 = []
list36 = []
for m in list00:
    num10 = m + 12
    num20 = m + 30
    num30 = m + 42
    num03 = m + 477
    num13 = num03 + 12
    num23 = num03 + 30
    num33 = num03 + 42
    num06 = num03 + 477
    num16 = num06 + 12
    num26 = num06 + 30
    num36 = num06 + 42
    list10.append(num10)
    list20.append(num20)
    list30.append(num30)
    list03.append(num03)
    list13.append(num13)
    list23.append(num23)
    list33.append(num33)
    list06.append(num06)
    list16.append(num16)
    list26.append(num26)
    list36.append(num36)

# 竖画同理。
list01 = [107, 159, 160, 161, 212, 213, 214, 265, 266, 267, 
          318, 319, 320, 371, 372, 373, 424, 425, 426, 478]
list11 = []
list21 = []
list31 = []
list02 = []
list12 = []
list22 = []
list32 = []
list04 = []
list14 = []
list24 = []
list34 = []
list05 = []
list15 = []
list25 = []
list35 = []
for n in list01:
    num11 = n + 12
    num21 = n + 30
    num31 = n + 42
    num02 = n + 8
    num12 = num02 + 12
    num22 = num02 + 30
    num32 = num02 + 42
    num04 = n + 477
    num14 = num04 + 12
    num24 = num04 + 30
    num34 = num04 + 42
    num05 = num04 + 8
    num15 = num05 + 12
    num25 = num05 + 30
    num35 = num05 + 42
    list11.append(num11)
    list21.append(num21)
    list31.append(num31)
    list02.append(num02)
    list12.append(num12)
    list22.append(num22)
    list32.append(num32)
    list04.append(num04)
    list14.append(num14)
    list24.append(num24)
    list34.append(num34)
    list05.append(num05)
    list15.append(num15)
    list25.append(num25)
    list35.append(num35)

# 将同一轮次7个开关的占位编号序列进行关联整合，形成4个序列之集合。后续循环可根据开关序数order索引某一开关的占位编号序列。
list_turn0 = [list00, list01, list02, list03, list04, list05, list06]
list_turn1 = [list10, list11, list12, list13, list14, list15, list16]
list_turn2 = [list20, list21, list22, list23, list24, list25, list26]
list_turn3 = [list30, list31, list32, list33, list34, list35, list36]
# 将对4个序列之集合放入序列，此时可根据轮次turn索引到某一轮涉及到的点位序列之集合。
list_turn = [list_turn0, list_turn1, list_turn2, list_turn3]


list_num = []  # 此处是需要用电子时钟显示的时间（四个数字表示）。先留空，交互后形成四位时间数序列。
time = input("这是一个电子时钟显示器。请输入一个时间，用连续的四位数表示（示例：1824）：")
for each in str(time):
    x = int(each)
    list_num.append(x)

for turn in range(0, 4):  # 外层循环：逐位判断。四位时间数，从左侧开始。
    num = list_num[turn]  # 从四位时间数中取出每轮的对象。
    list_switch = list_switches[num]  # 从开关总表中找到该数对应的开关序列。
    for order in range(0, 7):  # 中层：逐笔画判断，order为开关序数（正在判断哪一开关）。
        if list_switch[order] == 1:  # 依序判断每个开关，值为1时开关打开，需要操作；关闭则无需调整。
            for i in list_turn[turn][order]:  # 内层：逐点位判断。索引到每个开关可以控制的点位编号。
                list_total[i] = 1  # 在原有大坐标图的数字列表中，逐个将这些编号对应点位的0修改为1。

# 设置好时钟冒号的区域，相应点位批量改为1。整理好最右列需要添加换行的点位。
list_dot = [501, 502, 503, 554, 555, 556, 607, 608, 609, 
            978, 979, 980, 1031, 1032, 1033, 1084, 1085, 1086]
for t in list_dot:
    list_total[t] = 1

list_enter = [52, 52, 105, 158, 211, 264, 317, 370, 423, 476, 529, 582, 
              635, 688, 741, 794, 847, 900, 953, 1006, 1059, 1112,]

result = ""  # 输出结果初始为空。
for p in range(len(list_total)): # 遍历原有大空表。取1即改为“*”，取0即为空。
    if list_total[p] == 1:
        result += "*"
    if list_total[p] == 0:
        result += " "
    if p in list_enter:  # 处于换行位置的点，其后插入换行符。
        result += "\n"
    p += 1  #该轮次结束，继续循环。

print(result)  # 输出，完成。