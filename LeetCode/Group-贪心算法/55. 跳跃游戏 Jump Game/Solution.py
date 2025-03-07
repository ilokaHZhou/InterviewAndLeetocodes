"""
根据题目的描述，只要存在一个位置 x，它本身可以到达，并且它跳跃的最大长度为 x+nums[x]，这个值大于等于 y，即 x+nums[x]≥y，那么位置 y 也可以到达。

只要当前位置i小于之前遍历的数字的max_reach，那么它就是可以到达的
接下来只需要看当前位置i加上可以跳跃的步数nums[i]是否大于最后一个位置的索引n-1即可

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 当前能够到达的最远位置
        n = len(nums)

        for i in range(n):
            # 如果当前位置已经超过了 max_reach，说明无法继续跳跃
            if i > max_reach:
                return False
            # 更新 max_reach
            max_reach = max(max_reach, i + nums[i])
            print(max_reach)
            # 如果 max_reach 已经超过或等于最后一个位置，返回 True
            if max_reach >= n - 1:
                return True

        return False