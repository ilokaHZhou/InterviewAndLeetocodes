"""
雨水量等于左侧每个位置的 left_max， 与从右侧开始遍历，每个位置的 right_max这两个接水法的交集
也就是两者中在第i个位置的相对较小那个值（水平面）与对应height[i]的差，一致则为0，不一致意味着是凹坑，有蓄水

可以用双指针相对遍历，这样只需要一次循环，并且降低空间复杂度
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        # 初始化 left_max 和 right_max 数组
        left_max = [0] * n
        right_max = [0] * n

        # 计算 从左侧开始遍历，每个位置的 left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # 计算 从右侧开始遍历，每个位置的 right_max
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # 计算雨水量
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water