class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: # 滑动窗口法
        array_length = len(nums)
        left, right, min_len, accumulation = 0, 0, float('inf'), 0
        while right < array_length:
            accumulation += nums[right] # 窗口向右滑动
            while accumulation >= target: # 窗口到达题目要求，开始从左侧一点点缩小窗口
                subseq_length = right - left + 1
                min_len = min(min_len, subseq_length)
                accumulation -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0 # 如果不存在符合条件的子数组，返回 0 （所有数加起来都不够target值这种情况）