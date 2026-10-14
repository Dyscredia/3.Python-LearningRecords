print("数字炸弹游戏开始啦！请每轮输入一个数字，我将告诉你它与炸弹数的关系。",
      "看看你能多少轮猜出炸弹~\n我们的炸弹范围是(0,5]，且为整数。每轮猜测请输入不同数字~")
x = 3
A0 = input("请猜测：")
M0 = int(A0)
if M0 > x:
    print("太大啦！往小了猜")
    A1 = input("请猜测：")
    M1 = int(A1)
    if M1 > x:
        print("太大啦！往小了猜")
        A11 = input("请猜测：")
        M11 = int(A11)
        if M11 > x:
            print("太大啦！往小了猜")
            A111 = input("请猜测：")
            M111 = int(A111)
            if M111 > x:
                print("太大啦！往小了猜")
                A1111 = input("请猜测：")
                M1111 = int(A111)
                if M1111 == x:
                    print("猜对啦！你真棒~")
                else:
                    print("你是小笨猪！")
            else:
                if M111 < x:
                    print("太小啦！往大了猜")
                    A1112 = input("请猜测：")
                    M1112 = int(A1112)
                    if M1112 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    print("猜对啦！你真棒~")
        else:
            if M11 < x:
                print("太小啦！往大了猜")
                A112 = input("请猜测：")
                M112 = int(A112)
                if M112 > x:
                    print("太大啦！往小了猜")
                    A1121 = input("请猜测：")
                    M1121 = int(A1121)
                    if M1121 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M112 < x:
                        print("太小啦！往大了猜") 
                        A1122 = input("请猜测：") 
                        M1122 = int(A1122)
                        if M1122 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
               print("猜对啦！你真棒~")
    else:
        if M1 < x:
            print("太小啦！往大了猜")
            A12 = input("请猜测：")
            M12 = int(A12)
            if M12 > x:
                print("太大啦！往小了猜")
                A121 = input("请猜测：")
                M121 = int(A121)
                if M121 > x:
                    print("太大啦！往小了猜")
                    A1211 = input("请猜测：")
                    M1211 = int(A1211)
                    if M1211 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M121 < x:
                        print("太小啦！往大了猜")
                        A1212 = input("请猜测：")
                        M1212 = int(A1212)
                        if M1212 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
                if M12 < x:
                    print("太小啦！往大了猜")
                    A122 = input("请猜测：")
                    M122 = int(A122)
                    if M122 > x:
                        print("太大啦，往小了猜")
                        A1221 = input("请猜测：")
                        M1221 = int(A1221)
                        if M1221 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        if M122 < x:
                            print("太小啦！往大了猜")
                            A1222 = input("请猜测：")
                            M1222 = int(A1222)
                            if M1222 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    print("猜对啦！你真棒~")
        else:
            print("猜对啦！你真棒~")
else:
    if M0 < x:
        print("太小啦！往大了猜")
        A2 = input("请猜测：")
        M2 = int(A2)
        if M2 > x:
            print("太大啦！往小了猜")
            A21 = input("请猜测：")
            M21 = int(A21)
            if M21 > x:
                print("太大啦！往小了猜")
                A211 = input("请猜测：")
                M211 = int(A211)
                if M211 > x:
                    print("太大啦！往小了猜")
                    A2111 = input("请猜测：")
                    M2111 = int(A2111)
                    if M2111 == x:
                        print("猜对啦！你真棒~")
                    else:
                        print("你是小笨猪！")
                else:
                    if M211 < x:
                        print("太小啦！往大了猜")
                        A2112 = input("请猜测：")
                        M2112 = int(A2112)
                        if M2112 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        print("猜对啦！你真棒~")
            else:
                if M21 < x:
                    print("太小啦！往大了猜")
                    M212 = input("请猜测：")
                    if M212 > x:
                        print("太大啦！往小了猜")
                        A2121 = input("请猜测：")
                        M2121 = int(A2121)
                        if M2121 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪！")
                    else:
                        if M212 < x:
                            print("太小啦！往大了猜")
                            A2122 = input("请猜测：")
                            M2122 = int(A2122)
                            if M2122 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    print("猜对啦！你真棒~")
        else:
            if M2 < x:
                print("太小啦！往大了猜")
                A22 = input("请猜测：")
                M22 = int(A22)
                if M22 > x:
                    print("太大啦！往小了猜")
                    A221 = input("请猜测：")
                    M221 = int(A221)
                    if M221 > x:
                        print("太大啦！往小了猜")
                        A2211 = input("请猜测：")
                        M2211 = int(A2211)
                        if M2211 == x:
                            print("猜对啦！你真棒~")
                        else:
                            print("你是小笨猪")
                    else:
                        if M221 < x:
                            print("太小啦！往大了猜")
                            A2212 = input("请猜测：")
                            M2212 = int(A2212)
                            if M2212 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            print("猜对啦！你真棒~")
                else:
                    if M22 < x:
                        print("太小啦！往大了猜")
                        A222 = input("请猜测：")
                        M222 = int(A222)
                        if M222 > x:
                            print("太大啦！往小了猜")
                            A2221 = input("请猜测：")
                            M2221 = int(A2221)
                            if M2221 == x:
                                print("猜对啦！你真棒~")
                            else:
                                print("你是小笨猪！")
                        else:
                            if M222 < x:
                                print("太小啦！往大了猜")
                                A2222 = input("请猜测：")
                                M2222 = int(A2222)
                                if M2222 == x:
                                    print("猜对啦！你真棒~")
                                else:
                                    print("你是小笨猪！")
                            else:
                                print("猜对啦！你真棒~")
                    else:
                        print("猜对啦！你真棒~")
            else:
                print("猜对啦！你真棒~") 
    else:
        print("猜对啦！你真棒~")