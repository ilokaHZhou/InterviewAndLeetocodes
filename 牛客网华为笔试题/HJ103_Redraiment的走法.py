# 读取输入的台阶数量
n = int(input())
# 读取每个台阶的高度，存储在列表中
heights = list(map(int, input().split()))

# 初始化 dp 数组，dp[i] 表示以第 i 个台阶结尾的最长递增子序列的长度，初始值都为 1
dp = [1] * n

# 动态规划过程，计算以每个台阶结尾的最长递增子序列的长度
for i in range(n):
    for j in range(i):
        # 如果第 j 个台阶的高度小于第 i 个台阶的高度
        if heights[j] < heights[i]:
            # 更新 dp[i] 的值，取当前值和 dp[j] + 1 中的较大值
            dp[i] = max(dp[i], dp[j] + 1)

# 找出 dp 数组中的最大值，即为最长递增子序列的长度
result = max(dp)

# 输出结果
print(result)
