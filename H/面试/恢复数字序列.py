import sys
from collections import defaultdict

# 读取输入的打乱字符的字符串和正整数序列的长度
s, k = input().strip().split()
k = int(k)

# 创建一个字典，用于统计打乱字符的字符串中各字符的数量
base = defaultdict(int)
for c in s:
    base[c] += 1

# 初始化滑动窗口的起始位置
i = 1
# 当滑动窗口的起始位置小于等于1000减去序列长度加1时，继续循环
while i <= 1000 - k + 1:
    # 创建一个字典，用于计算滑动窗口内各字符的数量
    count = defaultdict(int)
    # 遍历滑动窗口内的正整数
    for j in range(i, i + k):
        # 将正整数转换为字符串
        num = str(j)
        # 遍历正整数字符串中的字符
        for c in num:
            # 将字符及其数量存入字典
            count[c] += 1

    # 初始化一个布尔变量，用于判断滑动窗口内各字符数量是否与打乱字符的字符串中各字符数量一致
    is_match = True
    # 遍历打乱字符的字符串中的字符
    for c in base:
        # 如果滑动窗口内的字符数量与打乱字符的字符串中的字符数量不一致，将is_match设为False并跳出循环
        if count[c] != base[c]:
            is_match = False
            break

    # 如果滑动窗口内各字符数量与打乱字符的字符串中各字符数量一致，则输出滑动窗口的起始位置并退出循环
    if is_match:
        print(i)
        break

    # 更新滑动窗口的起始位置
    i += 1