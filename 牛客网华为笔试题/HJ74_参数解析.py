def parse_arguments(s):
    args = []  # 存储解析后的参数
    i = 0
    n = len(s)
    while i < n:  # 遍历字符串
        if s[i] == " ":  # 跳过空格
            i += 1
        elif s[i] == '"':  # 处理双引号内的参数
            i += 1
            start = i
            while i < n and s[i] != '"':  # 找到下一个双引号
                i += 1
            args.append(s[start:i])  # 添加参数
            i += 1
        else:  # 处理普通参数
            start = i
            while i < n and s[i] != " ":  # 找到下一个空格
                i += 1
            args.append(s[start:i])  # 添加参数
    return args  # 返回解析后的参数列表


# 输入处理
s = input().strip()
args = parse_arguments(s)
print(len(args))  # 输出参数个数
for arg in args:  # 输出每个参数
    print(arg)
