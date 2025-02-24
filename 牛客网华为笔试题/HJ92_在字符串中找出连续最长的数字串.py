def longest_digit_string(s):
    max_len = 0  # 最长数字串的长度
    max_strs = []  # 存储所有最长数字串
    current_len = 0  # 当前数字串的长度
    current_str = ""  # 当前数字串

    for char in s:  # 遍历字符串
        if char.isdigit():  # 如果当前字符是数字
            current_len += 1  # 当前数字串长度加 1
            current_str += char  # 当前数字串追加字符
        else:  # 如果当前字符不是数字
            if current_len > max_len:  # 发现更长的数字串
                max_len = current_len
                max_strs = [current_str]  # 重置最长数字串列表
            elif current_len == max_len:  # 发现与当前最长长度相同的数字串
                max_strs.append(current_str)  # 添加到最长数字串列表
            current_len = 0  # 重置当前数字串
            current_str = ""
    # 检查最后一个数字串
    if current_len > max_len:  # 发现更长的数字串
        max_len = current_len
        max_strs = [current_str]
    elif current_len == max_len:  # 发现与当前最长长度相同的数字串
        max_strs.append(current_str)

    return "".join(max_strs), max_len  # 返回拼接的最长数字串及其长度


# 输入处理
s = input().strip()
result_str, result_len = longest_digit_string(s)
print(result_str + "," + str(result_len))
