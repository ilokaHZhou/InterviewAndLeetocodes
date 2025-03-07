"""
经典动态规划题
dp状态表里的每个值是截止当前房屋，前 i 间房屋能获得的最大收益
当前房屋可以是被偷的，也可以是被跳过不被偷的

被偷的：当前收益 = 当前房屋金额 + 跳过前一个再往前的（k-2）房屋的最大收益
不会被偷的： 当前收益 = 前一个房屋（k-1）的最大收益
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n-1]