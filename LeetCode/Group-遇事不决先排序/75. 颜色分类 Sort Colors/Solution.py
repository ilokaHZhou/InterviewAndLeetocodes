"""
相当于快排三路排序中的partition排序，因为数组只有三个可能的数字，因此用一套逻辑排一次即可，pivot看成是1
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l_index = 0
        r_index = n - 1
        i = 0
        while i <= r_index:
            if nums[i] == 0:
                nums[i], nums[l_index] = nums[l_index], nums[i]
                l_index += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r_index] = nums[r_index], nums[i]
                r_index -= 1
            else:
                i += 1
        