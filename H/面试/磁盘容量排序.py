import sys

# 读取磁盘数量
n = int(input())

# 存储处理后的磁盘容量及其原始字符串
res = []

# 处理n行磁盘容量
for _ in range(n):
    capacity = input()
    sum = 0
    left = 0
    right = 1

    # 将磁盘容量转化为数值
    while right < len(capacity):
        if capacity[right] in ['M', 'G', 'T']:
            val = int(capacity[left:right])
            if capacity[right] == 'M':
                sum += val  # M为基本单位
            elif capacity[right] == 'G':
                sum += val * 1024  # 1G = 1024M
            elif capacity[right] == 'T':
                sum += val * 1024 * 1024  # 1T = 1024G = 1024*1024M
            left = right + 1  # 更新左指针
        right += 1  # 移动右指针

    # 存储容量及其原始字符串
    res.append((sum, capacity))

# 按容量排序后输出
res.sort(key=lambda x: x[0])
for _, capacity in res:
    print(capacity)