
"""
**** ****   **** ****
*  * *  * * *  * *  *
**** ****   **** ****
*  * *  * * *  * *  *
**** ****   **** ****

Every number has 13 control bits, so we need 52 bit (boolean value) totally.
0~12 13~25 26~38 39~51

with corresponding index is:
0112 ****   **** ****
3  4 *  * * *  * *  *
5667 ****   **** ****
8  9 *  * * *  * *  *
ABBC ****   **** ****

so we need a 4 * 13 matrix to represent! here we use type list[list[bool]]
"""
CONTROL_BITS = 13
NUMBER_COUNTS = 4
PRINT_LINES = 5
PRINT_COLUMNS = 21
index_mapping = {
    0: 0,
    1: 3,
    2: 5,
    3: 8,
    4: 10
}
print_mapping = {
    True: '*',
    False: ' '
}
def present(data_list: list[list[bool]]):
    result = ""
    for line in range(PRINT_LINES):
        number_idx = 0
        for col in range(PRINT_COLUMNS):
            if col in [4, 9, 11, 16]:
                result += " "
                continue
            if col == 10:
                symbol = print_mapping[line in [1, 3]]
                result += symbol
                continue
            
            if col in [0, 5, 12, 17]:
                # for num in range(NUMBER_COUNTS):
                data = data_list[number_idx]
                begin = index_mapping[line]
                if line in [0, 2, 4]:    
                    symbols = print_mapping[data[begin]] + print_mapping[data[begin+1]] + print_mapping[data[begin+1]] + print_mapping[data[begin+2]]
                if line in [1, 3]:
                    symbols = print_mapping[data[begin]] + " " + " " + print_mapping[data[begin+1]]
                result += symbols
                    # pass # for num in range(NUMBER_COUNTS):
                number_idx += 1
                pass # if col in [0, 5, 12, 17]:
            pass # for col in range(PRINT_COLUMNS):
        result += "\n"
        pass # for line in range(PRINT_LINES):
    print(result)
    pass # def present(data_list: list[list[bool]]):

"""
0112 ****   **** ****
3  4 *  * * *  * *  *
5667 ****   **** ****
8  9 *  * * *  * *  *
ABBC ****   **** ****
"""
TEST_VALUE = [
    [True, True, True, True, True, True, False, True, True, True, True, True, True], # 0
    [True, True, True, False, True, False, False, True, False, True, False, False, True], # 7
    [False, False, True, False, True, False, False, True, False, True, False, False, True], # 1
    [True, True, True, True, False, True, True, True, True, True, True, True, True], # 6
]

# TEST_VALUE = [
#     [True, True, True, True, True, True, True, True, True, True, True, True, True], # 8
#     [True, True, True, True, True, True, True, True, True, True, True, True, True], # 8
#     [True, True, True, True, True, True, True, True, True, True, True, True, True], # 8
#     [True, True, True, True, True, True, True, True, True, True, True, True, True], # 8
# ]

present(TEST_VALUE)

def digital_timer():
    pass

