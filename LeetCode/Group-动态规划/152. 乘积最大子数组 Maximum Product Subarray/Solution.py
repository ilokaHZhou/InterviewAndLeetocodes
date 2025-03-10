"""
动态规划：
    由于数组中可能存在负数，负负得正可能会导致最大值变为最小值，最小值变为最大值。因此，我们需要同时维护两个状态：
    max_dp[i]：以 nums[i] 结尾的子数组的最大乘积。
    min_dp[i]：以 nums[i] 结尾的子数组的最小乘积。

状态转移方程：

如果 nums[i] 是正数：
    max_dp[i] = max(nums[i], max_dp[i-1] * nums[i])
    min_dp[i] = min(nums[i], min_dp[i-1] * nums[i])

如果 nums[i] 是负数：
    max_dp[i] = max(nums[i], min_dp[i-1] * nums[i])
    min_dp[i] = min(nums[i], max_dp[i-1] * nums[i])

初始化：
    max_dp[0] = nums[0]
    min_dp[0] = nums[0]

结果：
    最终结果是 max_dp 数组中的最大值。
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        max_dp = [0] * n
        min_dp = [0] * n
        max_dp[0] = min_dp[0] = nums[0]
        # 动态规划
        for i in range(1, n):
            if nums[i] >= 0:
                max_dp[i] = max(nums[i], max_dp[i-1] * nums[i])
                min_dp[i] = min(nums[i], min_dp[i-1] * nums[i])
            else:
                max_dp[i] = max(nums[i], min_dp[i-1] * nums[i])
                min_dp[i] = min(nums[i], max_dp[i-1] * nums[i])
            
            # 更新结果
            result = max(result, max_dp[i])

        return result