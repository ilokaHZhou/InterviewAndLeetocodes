import sys

for line in sys.stdin:
    a = line.split()
    # 1. 直接转换 print(int(a[0], 16))

    # 2. 不直接转换，从右往左，将第 i 位乘以 16^i，然后求和
    s = a[0].strip()

    # 去掉前缀 '0x'
    if s.startswith('0x'):
        s = s[2:]

    # 定义十六进制字符到十进制数的映射
    hex_to_dec = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    # 初始化结果
    decimal_number = 0

    # 从右往左遍历每一位
    for i, char in enumerate(reversed(s)):
        # 获取当前字符对应的十进制值
        value = hex_to_dec[char.upper()]
        # 计算当前位的权重：16^i
        weight = 16 ** i
        # 累加结果
        decimal_number += value * weight

    # 输出十进制数
    print(decimal_number)
