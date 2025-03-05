class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1) # 初始化动态规划数组，用 n+1是为了方便处理边界逻辑
        dp[1] = 1 # 一楼 爬 1 阶楼梯有 1 种方法
        dp[2] = 2 # 二楼 爬 2 阶楼梯有 2 种方法
        for i in range(3, n+1): # 从第 3 阶开始计算
            dp[i] = dp[i - 1] + dp[i - 2] # 状态转移方程！！！！
        return dp[n] 
