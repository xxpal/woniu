# ================================================================================
# P297 - 练习题4
# 创建一个列表，将第三个元素更改为'third'，输出整个列表。
# ================================================================================


def print_list(list_input: list = []):
    print('修改之前，列表为：', list_input)
    list_input[2] = 'third'
    print('修改之后，列表为：', list_input)

    return


print_list(list(input("请输入一个列表：")))
