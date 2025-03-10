"""
解题思路
将数组视为哈希表：

对于一个长度为 n 的数组，缺失的最小正整数一定在 [1, n+1] 范围内。

我们可以通过原地修改数组，将每个正整数 x 放到数组的 x-1 位置上。

最终遍历数组，找到第一个不满足 nums[i] == i + 1 的位置，返回 i + 1。

具体步骤：

遍历数组，将每个正整数 x 放到 nums[x-1] 的位置上。

如果 x 不在 [1, n] 范围内，或者 nums[x-1] 已经是正确的值，则跳过。

最后遍历数组，找到第一个不满足 nums[i] == i + 1 的位置，返回 i + 1。


这个思想就相当于我们自己编写哈希函数，这个哈希函数的规则特别简单，那就是数值为 i 的数映射到下标为 i - 1 的位置。
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 将每个正整数 x 放到 nums[x-1] 的位置上
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换 nums[i] 和 nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 找到第一个不满足 nums[i] == i + 1 的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果数组中的数都满足 nums[i] == i + 1，则返回 n + 1
        return n + 1
