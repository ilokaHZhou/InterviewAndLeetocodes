"""
只用返回下标，因此字典里存num: index，检测与num互补的数是否在hashmap里，有的话就返回对应index，没有就把当前遍历的num: index存进hashmap里
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hashmap:
                result = [i, hashmap[dif]]
                break
            hashmap[nums[i]] = i
        return result