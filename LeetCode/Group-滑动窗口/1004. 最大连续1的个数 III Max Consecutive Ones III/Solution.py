# 转化为求滑动窗口里面允许最大有k个0的前提下，滑动窗口的最大长度
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = count0 = result = 0
        for right, v in enumerate(nums):
            if v == 0: # count0 用来记录用了多少个翻转次数
                count0 += 1
            while count0 > k: # 不断更新滑动窗口左边界直到窗口里最多只有k个0
                if nums[left] == 0: # 左边有用到翻转次数则减少使用过的翻转次数
                    count0 -=1
                left += 1
            result = max(result, right - left + 1) # 左右边界都包括所以加1
        return result