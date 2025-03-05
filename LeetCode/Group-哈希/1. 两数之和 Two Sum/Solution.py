class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        for index in range(len(nums)):
            difference = target - nums[index]
            if (difference in hashmap.keys()):
                result = [hashmap[difference], index]
                break
            hashmap[nums[index]] = index
        return result