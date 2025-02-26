# 用于读取输入的标准库
import sys

# 用于存储输入行的数组
lines = []
# 读取标准输入
for line in sys.stdin:
    lines.append(line.strip())

# 披萨的数量
n = int(lines[0])
# 每块披萨的美味值
a = list(map(int, lines[1:1 + n]))
# 记忆化数组，用于存储已计算过的状态
dp = [[-1 for _ in range(n)] for _ in range(n)]

# 计算最大美味值的函数
def allocation(L, R):
    # 如果已计算过，直接返回结果
    if dp[L][R] != -1:
        return dp[L][R]
    # 根据美味值选择吃掉左边或右边的披萨
    if a[L] > a[R]:
        L = (L + 1) % n
    else:
        R = (R + n - 1) % n
    # 如果只剩一块披萨，返回其美味值
    if L == R:
        dp[L][R] = a[L]
    else:
        dp[L][R] = max(a[L] + allocation((L + 1) % n, R), a[R] + allocation(L, (R + n - 1) % n))
    return dp[L][R]

# 初始化最大美味值为 0
ans = 0
# 计算并更新最大美味值
for i in range(n):
    ans = max(ans, allocation((i + 1) % n, (i + n - 1) % n) + a[i])

# 输出最多能吃到的披萨的美味值总和
print(ans)