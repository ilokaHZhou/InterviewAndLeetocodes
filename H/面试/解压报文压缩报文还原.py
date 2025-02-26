compressed_string = input()
stack = [['', 1, '']]  # 使用栈来存储解压后的字符串和重复次数
current_str = ''  # 当前字符
current_num = ''  # 当前重复次数
for c in compressed_string:
    if c.isalpha():  # 如果是字母
        current_str += c
    elif c.isdigit():  # 如果是数字
        current_num += c
    elif c == '[':  # 如果是左括号
        stack.append([current_str, int(current_num), ''])  # 将当前字符和重复次数入栈
        current_str = current_num = ''  # 重置当前字符和重复次数
    else:  # 如果是右括号
        prev_str, times, prev_result = stack.pop()  # 弹出栈顶元素
        stack[-1][-1] += prev_str + times * (prev_result + current_str)  # 更新栈顶元素的结果
        current_str = ''  # 重置当前字符
result = stack.pop()[-1] + current_str  # 返回最终的结果
print(result)