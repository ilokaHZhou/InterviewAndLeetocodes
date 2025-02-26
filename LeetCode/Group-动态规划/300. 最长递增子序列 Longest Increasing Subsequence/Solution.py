"""
1. 普通动态规划
def lengthOfLIS(nums):
    if not nums:
        return 0
    
    # 初始化 dp 数组，每个元素至少可以构成长度为 1 的子序列
    dp = [1] * len(nums)
    
    # 遍历数组
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 返回 dp 数组中的最大值
    return max(dp)

2. 二分查找 + 贪心
"""

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            # 使用二分查找找到插入位置
            pos = bisect.bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)  # 如果 num 比所有元素都大，直接添加到末尾
            else:
                dp[pos] = num    # 否则替换掉第一个大于等于 num 的元素
        return len(dp)
