def mark_digits(s):
    result = []  # 存储结果
    i = 0
    while i < len(s):  # 遍历字符串
        if s[i].isdigit():  # 如果当前字符是数字
            result.append("*")  # 添加 '*' 标记
            while i < len(s) and s[i].isdigit():  # 遍历连续的数字
                result.append(s[i])  # 添加数字
                i += 1
            result.append("*")  # 添加 '*' 标记
        else:  # 如果当前字符不是数字
            result.append(s[i])  # 直接添加字符
            i += 1
    return "".join(result)  # 返回结果字符串


# 输入处理
s = input().strip()
print(mark_digits(s))
