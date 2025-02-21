"""
简单的贪心/双指针题，遇到下坡或者遍历结束将当前子序列长度与max做对比，取最大值
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 1
        slow, fast, maxLength = 0, 1, 0
        while fast < n:
            if nums[fast] <= nums[fast - 1]:
                maxLength = max(maxLength, fast - slow)
                slow = fast
            fast += 1
        return max(maxLength, fast - slow)

        