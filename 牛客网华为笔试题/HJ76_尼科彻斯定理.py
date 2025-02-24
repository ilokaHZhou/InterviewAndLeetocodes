def nico_cheese_theorem(m):
    start = m * m - m + 1  # 计算起始奇数
    sequence = [str(start + 2 * i) for i in range(m)]  # 生成连续奇数序列
    return "+".join(sequence)  # 返回拼接的字符串


# 输入处理
m = int(input())
print(nico_cheese_theorem(m))
