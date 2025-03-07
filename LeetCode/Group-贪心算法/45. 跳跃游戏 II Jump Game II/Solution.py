"""
1. 贪心找离当前位置最远的前一个位置，然后更新当前位置，时间复杂度O(n^2):
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps

2. 如果我们「贪心」地进行正向查找，每次找到可到达的最远位置，就可以在线性时间内得到最少的跳跃次数。
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # end为当前能够达到的最大位置的索引,也就是边界, 不断更新边界并在每次触及边界时将跳跃次数增加 1
        maxPos, end, steps = 0, 0, 0
        for i in range(n - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    steps += 1
        return steps