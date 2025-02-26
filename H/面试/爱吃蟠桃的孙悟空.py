import math

# 判断以速度k是否能在h小时内吃完所有桃子
def can_finish(p, h, k):
    ans = 0
    for x in p:
        ans += math.ceil(x / k)
    return ans <= h

# 读取输入
peach_counts = list(map(int, input().split()))
h = int(input())

# 输入验证
n = len(peach_counts)
if n == 0 or h <= 0 or n >= 10000 or h >= 10000 or n > h:
    print(0)
    exit(0)

# 二分查找最小吃桃速度
left, right = 1, int(1e9)
while left < right:
    mid = (left + right) // 2
    if can_finish(peach_counts, h, mid):
        right = mid
    else:
        left = mid + 1

# 输出最小吃桃速度
print(left)