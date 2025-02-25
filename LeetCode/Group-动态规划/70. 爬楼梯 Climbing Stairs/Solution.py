class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  # 如果楼梯数小于等于 2
            return n  # 直接返回 n
        dp = [0] * (n + 1)  # 初始化动态规划数组！！！！
        dp[1] = 1  # 爬 1 阶楼梯有 1 种方法
        dp[2] = 2  # 爬 2 阶楼梯有 2 种方法
        for i in range(3, n + 1):  # 从第 3 阶开始计算
            dp[i] = dp[i - 1] + dp[i - 2]  # 状态转移方程！！！！
        return dp[n]  # 返回爬 n 阶楼梯的方法数
