"""
sum=prefix_sum[right]−prefix_sum[left−1]

k = prefix_sum_current - prefix_sum_before

前缀和 + 哈希表优化：

前缀和：计算从数组开头到当前元素的累加和，记为 prefix_sum。

哈希表：使用哈希表记录每个前缀和出现的次数。

核心思想：如果存在 prefix_sum - k 在哈希表中，说明从某个位置到当前位置的子数组和为 k。
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化哈希表，记录前缀和出现的次数
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 # 前缀和为0的情况出现一次, 针对特殊情况子串从数组开头开始且和正好等于k
        prefix_sum = 0
        count  = 0

        for item in nums:
            prefix_sum += item
            prefix_sum_before = prefix_sum - k
            # 如果 prefix_sum - k 在哈希表中，说明存在子数组和为 k
            if prefix_sum_before in prefix_count:
                count += prefix_count[prefix_sum_before]
            # 更新当前前缀和的出现次数
            prefix_count[prefix_sum] += 1
        return count