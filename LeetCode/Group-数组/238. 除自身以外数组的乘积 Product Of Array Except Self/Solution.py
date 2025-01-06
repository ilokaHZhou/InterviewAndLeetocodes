# 推荐解法把从元素左侧的累乘数和右侧的累乘数做成两个数组，两个数组对应元素相乘就是答案
# 这里可以用双指针分别从两侧相向遍历累乘，每个数都是从左从右循环的对应前一个数累乘数的积，这样只需一个循环就能完成三个循环的工作
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [1] * len(nums)
        lp = rp = 1
        while left < len(nums) and right >= 0:
            result[right] = result[right] * rp
            result[left] = result[left] * lp
            lp = lp * nums[left]
            left = left + 1
            rp = rp * nums[right]
            right = right - 1
        return result