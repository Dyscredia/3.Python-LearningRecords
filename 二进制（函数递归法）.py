def convert_decimal_to_binary(decimal: int) -> str:
    if decimal < 2: 
        return str(decimal)
    return convert_decimal_to_binary(decimal // 2) + str(decimal % 2)


x = input("请输入任意一个正整数：")

print(convert_decimal_to_binary(int(x)))