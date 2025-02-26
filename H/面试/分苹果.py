import sys

# 读取苹果的数量 n
n = int(input())
# 读取每个苹果的重量并存储到列表 a 中
a = list(map(int, input().split()))

# 初始化异或总和
sums = 0
# 初始化最小值为系统的最大整数
min_val = sys.maxsize
# 遍历所有苹果的重量
for x in a:
    # 按位异或操作，更新异或总和
    sums = sums ^ x
    # 找到当前最小的苹果重量
    if x < min_val:
        min_val = x

# 如果异或总和不为 0，则无法按 A 的规则分堆，输出 -1
if sums != 0:
    print(-1)
else:
    # 计算所有苹果重量的总和
    total_sum = sum(a)
    # 输出 B 可以获取的最大苹果重量（总和减去最小的苹果重量）
    print(total_sum - min_val)