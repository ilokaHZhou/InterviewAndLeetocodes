# 滑动窗口看作是胃口为1的贪吃蛇，吃1头部增长尾部不变，吃0头尾皆向前移动一格
# 最终长度即为最长子串长度
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        count0 = 1
        while right < len(nums):
            if nums[right] == 0:
                count0 -= 1
            if count0 < 0:
                if nums[left] ==0:
                    count0 += 1
                left += 1
            right += 1
        return right - left - 1