def count_uppercase(s):
    count = 0  # 初始化计数器
    for char in s:  # 遍历字符串
        if char.isupper():  # 判断是否为大写字母
            count += 1  # 计数器加 1
    return count  # 返回大写字母个数


# 输入处理
s = input().strip()
print(count_uppercase(s))
