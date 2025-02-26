def main():
    # 读取用户输入并使用空格分隔
    input_sequence = input().split()
    # 创建一个列表用作数字栈
    number_stack = []

    # 遍历输入的数字序列
    for number_string in input_sequence:
        # 将字符串转换为整数
        current_number = int(number_string)
        # 初始化部分和为当前数字
        partial_sum = current_number

        # 从栈顶向栈底检查是否满足出栈条件
        index = len(number_stack) - 1
        while index >= 0:
            # 从部分和中减去栈中的元素
            partial_sum -= number_stack[index]

            # 如果满足出栈条件，清除子列表并更新当前数字
            if partial_sum == 0:
                # 清除子列表
                number_stack = number_stack[:index]
                # 更新当前数字
                current_number *= 2
                # 更新部分和
                partial_sum = current_number
            elif partial_sum < 0:
                # 如果部分和小于0，跳出循环
                break

            index -= 1

        # 将当前数字入栈
        number_stack.append(current_number)

    # 输出栈中的元素，从栈顶到栈底
    output = ' '.join(map(str, reversed(number_stack)))
    print(output)


if __name__ == "__main__":
    main()