class Solution:
    def maxSubArray(self, nums): # 如果当前总和为负数，赶紧抛弃，重置count为0从下一个正数开始重新计总和
        max_sum = current_sum = nums[0]  # 初始化为数组的第一个元素
        for num in nums[1:]:  # 从第二个元素开始遍历
            current_sum = max(num, current_sum + num)  # 更新当前和
            max_sum = max(max_sum, current_sum)  # 更新最大和
        return max_sum  # 返回最大区间和