def count_ones(n):
    count = 0  # 初始化计数器，计1的个数
    while n > 0:  # 当 n 大于 0 时循环
        count = count + (n & 1)  # 检查最低位是否为 1
        n >>= 1  # 右移一位，去掉最低位
    return count  # 返回 1 的个数

# 输入处理
n = int(input())
print(count_ones(n))
m = int(input())
print(count_ones(m))