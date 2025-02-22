def remove_least_frequent_chars(s):
    # 统计每个字符的出现次数
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1 # get(char, 0) char不存在时返回0

    # 找到最小出现次数
    min_freq = min(freq.values())

    # 删除出现次数最少的字符
    result = "".join([char for char in s if freq[char] != min_freq])

    return result


# 读取输入
s = input().strip()
# 输出结果
print(remove_least_frequent_chars(s))
