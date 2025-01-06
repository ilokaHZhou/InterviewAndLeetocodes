'''
用贪心算法，为了找到递增的三元子序列，first 和 second 应该尽可能地小，此时找到递增的三元子序列的可能性更大。
初始时，first=nums[0]，second=+∞。对于 1≤i<n，当遍历到下标 i 时，令 num=nums[i]，进行如下操作：

1. 如果 num>second，则找到了一个递增的三元子序列，返回 true；
2. 否则，如果 num>first，则将 second 的值更新为 num；
3. 否则，将 first 的值更新为 num, 继续遍历找第三个数。
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = nums[0]
        second = float('inf')
        for i, v in enumerate(nums):
            if v > second:
                return True
            elif v > first:
                second = v
            else:
                first = v
        return False
