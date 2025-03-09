"""
dp[i] 表示凑成金额 i 所需的最少硬币数

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        # 初始化 dp 数组，大小为 amount + 1，初始值为无穷大
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 凑成金额 0 需要 0 个硬币

        # 遍历每个金额, 因为要包含amount所以右边界是amount+1
        for i in range(1, amount + 1):
            # 遍历每个硬币,用来算凑成金额 i 所需的硬币数
            for coin in coins:
                if coin <= i:
                    # 更新 dp[i]
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 如果 dp[amount] 仍然是初始值，表示无法凑成该金额
        return dp[amount] if dp[amount] != float('inf') else -1