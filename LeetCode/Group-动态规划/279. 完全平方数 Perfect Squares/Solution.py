"""
dp[i] 表示组成整数 i 的最少完全平方数的数量

dp[i - j * j] + 1 是指前一个完全平方数到当前完全平方数需要一个额外的平方数
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化 dp 数组，大小为 n+1，初始值为无穷大
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 组成 0 需要 0 个完全平方数

        # 遍历每个整数 i
        for i in range(1, n + 1):
            # 遍历所有可能的完全平方数 j*j
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]