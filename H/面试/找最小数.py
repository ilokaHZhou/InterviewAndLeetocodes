# 读取输入的正整数 NUM1 和需要移除的数字个数
num = input()
k = int(input())

# 初始化一个栈，用于存储需要保留的数字
stack = []

# 遍历 NUM1 中的每个字符
for i in num:
    # 当栈非空、需要移除的数字个数大于 0 且栈顶元素大于当前字符时
    # 出栈并减少需要移除的数字个数
    while stack and k and stack[-1] > i:
        k -= 1
        stack.pop()
    # 将当前字符入栈
    stack.append(i)

# 输出结果字符串，移除剩余的数字，并去除前导零，如果为空则输出 "0"
print(''.join(stack[:len(stack) - k]).lstrip('0') or "0")
