input_str = input().strip()

# 九宫格枚举信息
char_map = {
    '0': ' ',
    '1': ',.',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

res = ""
# 默认是数字模式
mode = 0

i = 0
while i < len(input_str):
    c = input_str[i]
    if c.isdigit():  # 如果是数字
        if mode == 0:  # 如果是数字模式，直接加入结果
            res += c
        elif mode == 1:  # 如果是字母模式
            j = i
            tempstr = char_map[c]
            while j < len(input_str) and input_str[j] == c:  # 统计连续出现的数字个数
                j += 1
            index = (j - i - 1) % len(tempstr)  # 计算对应的字母下标
            res += tempstr[index]  # 加入结果
            i = j - 1  # 跳过已经处理的数字
    elif c == '#':  # 如果是切换模式符号
        mode = (mode + 1) % 2  # 切换模式
    elif c == '/':  # 如果是延迟符号，不做处理
        pass
    else:  # 如果是其他字符，直接退出循环
        break
    i += 1

print(res)  # 输出结果