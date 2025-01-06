# 双指针快慢指针即可解答
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        record = traverse = 1
        while traverse < len(nums):
            item = nums[traverse]
            if item != nums[traverse - 1]:
                nums[record] = item
                record += 1
            traverse += 1
        return record
